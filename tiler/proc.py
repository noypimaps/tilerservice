from django.conf import settings
import os

tile_output = settings.TILE_OUTPUT
warp_output = settings.WARP_OUTPUT
color_output = settings.COLOR_OUTPUT
color_text = "color-text.txt"


class ProcessAPI():
    def __init__(self):
        self.name = "Process API"

    def color_raster(self, rastname, input_raster, colorfile_loc=color_text):
        if os.path.isdir("%s/" % color_output):
            pass
        else:
            os.makedirs("%s/" % color_output)

        try:
            cmd = 'gdaldem color-relief -alpha %s %s %s/%s.tif' % (
                input_raster, colorfile_loc, color_output, rastname)

            os.system(cmd)
            color_loc = '%s/%s.tif' % (color_output, rastname)
            return ("Finished coloring %s" % rastname, "sucess", color_loc)
        except:
            return ("Failed coloring %s" % rastname, "failed")

    def warp_raster(self, rastname, input_raster):
        if os.path.isdir("%s/" % warp_output):
            pass
        else:
            os.makedirs("%s/" % warp_output)

        try:
            cmd = 'gdalwarp -co TILED=YES -co COMPRESS=DEFLATE -s_srs EPSG:4326 -t_srs EPSG:3857 %s %s/%s.tif' % (
                input_raster, warp_output, rastname)
            os.system(cmd)
            warp_loc = '%s/%s.tif' % (warp_output, rastname)
            return ("Finished warping %s" % rastname, "sucess", warp_loc)
        except:
            return ("Failed tiling %s" % rastname, "failed")

    def tile_raster(self, rastname, input_raster, zoom_levels="6-7"):
        try:
            cmd = 'gdal2tiles.py -z %s %s %s/%s' % (
                zoom_levels, input_raster, tile_output, rastname)
            os.system(cmd)
            return ("Finished tiling %s" % rastname, "sucess")
        except:
            return ("Failed tiling %s" % rastname, "failed")
