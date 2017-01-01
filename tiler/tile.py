import os
tile_output = "tile_output"
warp_output = "warp_output"
color_output = "color_output"


def warp_raster(rastname, input_raster):
    if os.path.isdir("%s/" % warp_output):
        pass
    else:
        os.makedirs("%s/" % warp_output)

    try:
        cmd = 'gdalwarp -co TILED=YES -co COMPRESS=DEFLATE -t_srs EPSG:3857 %s %s/%s.tif' % (
            input_raster, warp_output, rastname)
        os.system(cmd)
        return ("Finished warping %s" % rastname, "sucess")
    except:
        return ("Failed tiling %s" % rastname, "failed")


def tile_raster(rastname, input_raster, zoom_levels="6-7"):
    try:
        cmd = 'gdal2tiles.py -p raster -z %s %s %s/%s' % (
            zoom_levels, input_raster, tile_output, rastname)
        os.system(cmd)
        return ("Finished tiling %s" % rastname, "sucess")
    except:
        return ("Failed tiling %s" % rastname, "failed")


def color_raster(rastname, input_raster, colorfile_loc="color-text.txt"):
    if os.path.isdir("%s/" % color_output):
        pass
    else:
        os.makedirs("%s/" % color_output)

    try:
        cmd = 'gdaldem color-relief -alpha %s %s %s/%s.tif' % (
            input_raster, colorfile_loc, color_output, rastname)

        os.system(cmd)
        return ("Finished coloring %s" % rastname, "sucess")
    except:
        return ("Failed coloring %s" % rastname, "failed")


# tile_raster("test", "test.jpg", "6-7")
# warp_raster("test", "bathymetry.tif")
color_raster("test", "bathymetry.tif")
