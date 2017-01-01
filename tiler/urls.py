from django.conf.urls import url
from views import TileView
from views import TileWeb
from views import FileUploader


urlpatterns = [
    url(r'^tiler/$', TileView.as_view()),
    url(r'^upload/$', FileUploader.as_view()),
    url(r'^', TileWeb.as_view()),
]
