from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .proc import ProcessAPI


class TileView(View):
    def get(self, request):
        message = {}
        proc = ProcessAPI()
        input_raster = "sample_data/bathymetry.tif"
        color_text = "sample_data/color-text.txt"
        rastname = "test"
        proc.color_raster(rastname, input_raster, color_text)
        message['detail'] = proc.name
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
