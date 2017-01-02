from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .proc import ProcessAPI
from .uploader import UploaderAPI


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

    def post(self, request):
        message = {}
        message['detail'] = "File Uploader Post"
        upload = UploaderAPI()
        upload.upload_file(
            request.FILES['file'], request.POST.get('rastername'))
        return redirect('/')
