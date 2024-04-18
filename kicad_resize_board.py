"""
Regex replace the references of the selected footprints.
"""

import re
import pcbnew
import os
import wx
import logging
import math

from .dialog import ConfigDialog, Config

class ResizeBoardPlugin(pcbnew.ActionPlugin):
    logger = logging.getLogger(__name__)
    log_handler = None

    def defaults(self):
        self.name = "ResizeBoard"
        self.category = "pcbnew, footprints, resize"
        self.description = "Resize a board along with its gnd planes and mounting holes."
        self.show_toolbar_button = False # Optional, defaults to False
        # self.icon_file_name = os.path.join(os.path.dirname(__file__), 'simple_plugin.png') # Optional, defaults to ""
        self.config = None

    def iterateVertices(shapePolySet, callback):
        '''
        callback(v, io, ih, iv)
        '''
        o0 = shapePolySet
        for io in range(o0.OutlineCount()):
            for ih in range(-1, o0.HoleCount(io)):
                for iv in range(o0.VertexCount(io, ih)):
                    v = o0.CVertex(iv, io, ih)
                    callback(v, io, ih, iv)

    def Run(self):
        board = pcbnew.GetBoard()

        #SHAME Guess I could use GetCurrentSelection haha, eh, oh well, this is kinda easier

        errors = []

        # Find edge rect
        selected_drawings = [item for item in board.Drawings() if item.IsSelected()]
        boundary = None
        for d in selected_drawings:
            if d.ShowShape() == 'Rect':
                if boundary is not None:
                    errors.append('More than one rectangle drawing selected!  Only expecting one board edge.')
                boundary = d
        if boundary is None:
            errors.append('No rectangle drawing selected!  Expecting one board edge.')

        if len(errors) > 0:
            errors
            wx.MessageBox("Encountered errors:\n"+'\n'.join(errors), "ResizeBoard")
            return

        dialog = ConfigDialog()

        try:
            b_start = boundary.GetStart()
            b_end = boundary.GetEnd()
            
            if self.config is None:
                self.config = Config()
                

            self.config.new_width = pcbnew.ToMM(b_end.x - b_start.x)
            self.config.new_height = pcbnew.ToMM(b_end.y - b_start.y)
            dialog.SetConfig(self.config)

            if dialog.ShowModal() != wx.ID_OK:
                return

            #RAINY Save settings?
            self.config = dialog.GetConfig()

            # Resize board
            b_start = boundary.GetStart()
            b_end = boundary.GetEnd()
            b_start_orig = pcbnew.VECTOR2I(b_start.x, b_start.y)
            b_end_orig = pcbnew.VECTOR2I(b_end.x, b_end.y)
            print("before", b_start_orig, b_end_orig)
            boundary.SetEnd(boundary.GetStart()+pcbnew.VECTOR2I_MM(self.config.new_width, self.config.new_height))
            b_start = boundary.GetStart()
            b_end = boundary.GetEnd()
            print("after", b_start_orig, b_end_orig)
            print("afte2", b_start, b_end)

            # Find gnd planes
            selected_zones = [item for item in board.Zones() if item.IsSelected()]
            for z in selected_zones:
                o = z.Outline()

                tl = None
                br = None

                def findCorners(v, io, ih, iv):
                    nonlocal tl, br
                    if tl is None:
                        tl = pcbnew.VECTOR2I(v.x, v.y)
                    if br is None:
                        br = pcbnew.VECTOR2I(v.x, v.y)
                    if v.x < tl.x:
                        tl.x = v.x
                    if v.y < tl.y:
                        tl.y = v.y
                    if v.x > br.x:
                        br.x = v.x
                    if v.y > br.y:
                        br.y = v.y

                def transform_poly_set(poly, transform_point):
                    self.logger.debug("Polygon shape has %d outlines", poly.OutlineCount())

                    for i in range(poly.OutlineCount()):
                        outline: pcbnew.SHAPE_LINE_CHAIN = poly.Outline(i)
                        self.logger.debug("Outline has %d vertices and %d holes", outline.PointCount(), poly.HoleCount(i))

                        for pi in range(outline.PointCount()):
                            point = outline.CPoint(pi)
                            outline.SetPoint(pi, transform_point(point))
                        
                        for hi in range(poly.HoleCount(i)):
                            hole: pcbnew.SHAPE_LINE_CHAIN = poly.Hole(i, hi)
                            self.logger.debug("Hole has %d vertices", hole.PointCount())

                            for pi in range(hole.PointCount()):
                                point = hole.CPoint(pi)
                                hole.SetPoint(pi, transform_point(point))

                ResizeBoardPlugin.iterateVertices(z.Outline(), findCorners)
                if tl is not None:
                    def _transform_point(point, translate, center, x_scale, y_scale, angle):
                        x = point.x - center.x
                        y = point.y - center.y

                        # scale
                        x *= x_scale
                        y *= y_scale

                        # rotate
                        x, y = (
                            x * math.cos(angle) - y * math.sin(angle),
                            x * math.sin(angle) + y * math.cos(angle)
                        )

                        return pcbnew.VECTOR2I(center.x + int(x) + translate.x, center.y + int(y) + translate.y)
                    
                    def _tp0(point):
                        pitl = pcbnew.VECTOR2I_MM(self.config.planes_inset_left, self.config.planes_inset_top)
                        pibr = pcbnew.VECTOR2I_MM(self.config.planes_inset_right, self.config.planes_inset_bottom)

                        translate = pcbnew.VECTOR2I(b_start.x - tl.x + pitl.x, b_start.y - tl.y + pitl.y)
                        scale_x = (b_end.x-b_start.x-(pitl.x+pibr.x))/(br.x-tl.x)
                        scale_y = (b_end.y-b_start.y-(pitl.y+pibr.y))/(br.y-tl.y)

                        return _transform_point(point, translate, tl, scale_x, scale_y, 0)
                    
                    transform_poly_set(o, _tp0)
                z.HatchBorder()

            # Move presumed mounting holes
            selected_footprints = [item for item in board.Footprints() if item.IsSelected()]
            for f in selected_footprints:
                fc = f.GetCenter()
                btlo = b_start_orig
                bbro = b_end_orig
                btro = pcbnew.VECTOR2I(bbro.x, btlo.y)
                bblo = pcbnew.VECTOR2I(btlo.x, bbro.y)
                btln = b_start
                bbrn = b_end
                btrn = pcbnew.VECTOR2I(bbrn.x, btln.y)
                bbln = pcbnew.VECTOR2I(btln.x, bbrn.y)

                bc = None
                if abs(fc.x-btlo.x) < abs(fc.x-bbro.x):
                    # Closer to left side
                    if abs(fc.y-btlo.y) < abs(fc.y-bbro.y):
                        # Closer to top side
                        bc = pcbnew.VECTOR2I(btln.x, btln.y)+pcbnew.VECTOR2I_MM(+self.config.mounts_inset_left,+self.config.mounts_inset_top)
                    else:
                        # Closer to bottom side
                        bc = pcbnew.VECTOR2I(bbln.x, bbln.y)+pcbnew.VECTOR2I_MM(+self.config.mounts_inset_left,-self.config.mounts_inset_bottom)
                else:
                    # Closer to right side
                    if abs(fc.y-btlo.y) < abs(fc.y-bbro.y):
                        # Closer to top side
                        bc = pcbnew.VECTOR2I(btrn.x, btrn.y)+pcbnew.VECTOR2I_MM(-self.config.mounts_inset_right,+self.config.mounts_inset_top)
                    else:
                        # Closer to bottom side
                        bc = pcbnew.VECTOR2I(bbrn.x, bbrn.y)+pcbnew.VECTOR2I_MM(-self.config.mounts_inset_right,-self.config.mounts_inset_bottom)

                f.Move(bc-fc)

            
            # Refill zones
            zf = pcbnew.ZONE_FILLER(pcbnew.GetBoard())
            zones_to_refill = pcbnew.ZONES()
            for z in selected_zones:
                zones_to_refill.append(z)
            zf.Fill(zones_to_refill)

            pcbnew.Refresh()
        finally:
            dialog.Destroy()
    
ResizeBoardPlugin().register()



# Scratch
quit()


import pcbnew
board = pcbnew.GetBoard()

selected_items = [item for item in board.Footprints() if item.IsSelected()]

errors = []

# Find edge rect
selected_drawings = [item for item in board.Drawings() if item.IsSelected()]
rect = None
for d in selected_drawings:
    if d.ShowShape() == 'Rect':
        if rect is not None:
            errors.append('More than one rectangle drawing selected!  Only expecting one board edge.')
        rect = d
if rect is None:
    errors.append('No rectangle drawing selected!  Expecting one board edge.')

# Find gnd planes
selected_zones = [item for item in board.Zones() if item.IsSelected()]
for z in selected_zones:
    o = z.Outline()

z0 = selected_zones[0]

def blah():
    tl = None
    br = None

    def findCorners(v, io, ih, iv):
        nonlocal tl, br
        if tl is None:
            tl = pcbnew.VECTOR2I(v.x, v.y)
        if br is None:
            br = pcbnew.VECTOR2I(v.x, v.y)
        if v.x < tl.x:
            tl.x = v.x
        if v.y < tl.y:
            tl.y = v.y
        if v.x > br.x:
            br.x = v.x
        if v.y > br.y:
            br.y = v.y

    iterateVertices(z0.Outline(), findCorners)
    print(tl, br)

blah()
