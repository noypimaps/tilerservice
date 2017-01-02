from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import View
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
from .proc import ProcessAPI
from .uploader import UploaderAPI
from .models import RasterStore, TileStore
import json
import uuid
import shutil


class TileWeb(View):
    def get(self, request):
        message = {}
        message['detail'] = "Tile Web Interface"
        return render(request, "index.html")


class FileUploader(View):
    def post(self, request):
        message = {}
        message['detail'] = "File Uploader Post"
        upload = UploaderAPI()
        message = upload.upload_file(
            request.FILES['file'], request.FILES['colorfile'],
            request.POST.get('rastername'))
        rastname = request.POST.get('rastername')
        generate_tiles(rastname)

        if message[1] == 'error':
            return redirect('/')
        else:
            return redirect('/')


class RastersListAPI(View):
    def get(self, request):
        rasterlist = RasterStore.objects.all()
        data = json.loads(serializers.serialize(
            'json', rasterlist, fields=('layername')))
        return JsonResponse(data, safe=False)


class TileListAPI(View):
    def get(self, request):
        tilelist = TileStore.objects.all()
        data = json.loads(serializers.serialize(
            'json', tilelist, fields=('layername', 'link')))
        return JsonResponse(data, safe=False)


class DownloadTiles(View):
    def get(self, request, rastname):
        tile = TileStore.objects.get(layername=rastname)
        fileloc = tile.raw_location
        tmp_zipped = '/tmp/%s-%s' % (uuid.uuid1(), rastname)
        shutil.make_archive(tmp_zipped, 'zip', fileloc)
        wrapper = FileWrapper(file(tmp_zipped + '.zip'))
        response = HttpResponse(wrapper, content_type='application/zip')
        response[
            'Content-Disposition'] = 'attachment; filename=%s' % smart_str(tmp_zipped + '.zip')
        # response['X-Accel-Redirect'] = "/protected/{0}".format(document.file.name)
        return response
        # return HttpResponse('boom')


def generate_tiles(rastname):
    raster = get_object_or_404(RasterStore, layername=rastname)
    proc = ProcessAPI()
    input_raster = raster.raw_location
    color_text = raster.color_location
    rastname = raster.layername
    color_out = proc.color_raster(rastname, input_raster, color_text)
    warp_out = proc.warp_raster(rastname, color_out[2])
    proc.tile_raster(rastname, warp_out[2], settings.TILE_ZOOM)
