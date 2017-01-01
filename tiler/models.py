from __future__ import unicode_literals

from django.db import models


class TileStore(models.Model):
    layername = models.CharField(max_length=255)
    link = models.TextField()
    raw_location = models.TextField()

    def __unicode__(self):
        return self.layername
