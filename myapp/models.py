# Create your models here.

# models.py
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)
    comunidad = models.IntegerField()
    primer_nivel = models.IntegerField()
    segundo_nivel = models.IntegerField()
    centros = models.IntegerField()

