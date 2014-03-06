from django.db import models

class Corgi(models.Model):
  name = models.CharField(max_length=200)
  weight = models.IntegerField()
