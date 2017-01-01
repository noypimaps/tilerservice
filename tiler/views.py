from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .proc import ProcessAPI
# Create your views here.


class TileView(View):
    def get(self, request):
        message = {}
        proc = ProcessAPI()
        input_raster = "sample_data/bathymetry.tif"
        color_text = "sample_data/color-text.txt"
        proc.color_raster("test", input_raster, color_text)
        message['detail'] = proc.name
        return JsonResponse(message)
