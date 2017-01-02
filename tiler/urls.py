from django.conf.urls import url
from views import TileWeb
from views import FileUploader
from views import RastersListAPI
from views import TileListAPI
from views import DownloadTiles


urlpatterns = [
    url(r'^upload/$', FileUploader.as_view()),
    url(r'^download/(?P<rastname>\w+)/$', DownloadTiles.as_view()),
    url(r'^raster/list/$', RastersListAPI.as_view()),
    url(r'^tile/list/$', TileListAPI.as_view()),
    url(r'^', TileWeb.as_view()),
]
