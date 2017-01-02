from django.conf import settings
from models import RasterStore
from osgeo import gdal
import os

rast_store = settings.TILE_UPLOAD


class UploaderAPI():
    def __init__(self):
        self.name = "Uploader API"

    def store_to_db(self, rastname, loc):
        RasterStore.objects.create(layername=rastname, raw_location=loc)

    def check_raster(self, loc):
        try:
            gdal.Open(loc)
            return True
        except:
            return False

    def upload_file(self, f, rastname):
        raw_loc = rast_store + '/%s.tif' % rastname
        if os.path.isdir(rast_store):
            pass
        else:
            os.makedirs(rast_store)
        with open(raw_loc, 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
            self.store_to_db(rastname, raw_loc)
        return ("Finished storing %s" % rastname, "success")
