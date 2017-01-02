from __future__ import unicode_literals

from django.db import models


class TileStore(models.Model):
    layername = models.CharField(max_length=255, unique=True)
    link = models.TextField()
    raw_location = models.TextField()

    def __unicode__(self):
        return self.layername


class RasterStore(models.Model):
    layername = models.CharField(max_length=255, unique=True)
    raw_location = models.TextField()
    color_location = models.TextField(blank=True)

    def __unicode__(self):
        return self.layername
