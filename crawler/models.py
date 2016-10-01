from __future__ import unicode_literals

from django.db import models

class post_info(models.Model):
    message = models.TextField()
    story = models.TextField(blank=True)
    time = models.DateTimeField(blank=True)
    id = models.CharField(primary_key=True, max_length = 100)
    no_of_likes = models.IntegerField(blank=True)
    category = models.CharField(max_length=10,blank=True)
