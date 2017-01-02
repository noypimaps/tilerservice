from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.conf import settings
from django.http import JsonResponse
from .proc import ProcessAPI
from .uploader import UploaderAPI
from .models import RasterStore


class TileView(View):
    def get(self, request, rastname):
        message = {}
        raster = get_object_or_404(RasterStore, layername=rastname)
        proc = ProcessAPI()
        # input_raster = "sample_data/bathymetry.tif"
        # color_text = "sample_data/color-text.txt"
        # rastname = "test"
        input_raster = raster.raw_location
        color_text = raster.color_location
        rastname = raster.layername
        color_out = proc.color_raster(rastname, input_raster, color_text)
        warp_out = proc.warp_raster(rastname, color_out[2])
        # proc.tile_raster(rastname, warp_out[2], settings.TILE_ZOOM)
        message['detail'] = "finished warping"
        return JsonResponse(message)


class TileWeb(View):
    def get(self, request):
        message = {}
        message['detail'] = "Tile Web Interface"
        return render(request, "index.html")


class FileUploader(View):
    def get(self, request):
        message = {}
        message['detail'] = "File Uploader"
        return JsonResponse(message)

    def post(self, request):
        message = {}
        message['detail'] = "File Uploader Post"
        upload = UploaderAPI()
        message = upload.upload_file(
            request.FILES['file'], request.FILES['colorfile'],
            request.POST.get('rastername'))
        if message[1] == 'error':
            return redirect('/')
        else:
            return redirect('/')
