from django.conf.urls import url
from views import TileView

urlpatterns = [
    url(r'^tiler/$', TileView.as_view()),
]
