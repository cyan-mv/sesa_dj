from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

class DataEntry(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    values = models.JSONField()

    class Meta:
        unique_together = ('region', 'category')
