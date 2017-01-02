from django.conf import settings
from models import RasterStore
from osgeo import gdal
import os

rast_store = settings.TILE_UPLOAD


class UploaderAPI():
    def __init__(self):
        self.name = "Uploader API"

    def store_to_db(self, rastname, loc, colorloc):
        RasterStore.objects.create(
            layername=rastname, raw_location=loc, color_location=colorloc)

    def check_raster(self, loc):
        try:
            gdal.Open(loc)
            return True
        except:
            return False

    def upload_file(self, f, colorfile, rastname):
        raw_loc = rast_store + '/%s/%s.tif' % (rastname, rastname)
        color_loc = rast_store + '/%s/%s.txt' % (rastname, rastname)
        try:
            RasterStore.objects.get(layername=rastname)
            return ("%s has duplicate" % rastname, "error")
        except:
            pass

        if os.path.isdir(rast_store + '/%s' % rastname):
            pass
        else:
            os.makedirs(rast_store + '/%s' % rastname)

        with open(raw_loc, 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)

        with open(color_loc, 'wb+') as dest:
            for chunk in colorfile.chunks():
                dest.write(chunk)

        self.store_to_db(rastname, raw_loc, color_loc)
        return ("Finished storing %s" % rastname, "success")
