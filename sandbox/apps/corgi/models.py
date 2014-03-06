from django.db import models

class Corgi(models.Model):
  name = models.CharField(max_length=200)
  weight = models.IntegerField(null=True, blank=True, default=10)
  length = models.IntegerField(null=True, blank=True, default=5)
  description = models.CharField(max_length=200, blank=True)
