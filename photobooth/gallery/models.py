from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
'''
Image
Image Name.
Image Description.
Image Location Foreign Key.
Image category Foreign Key.
'''
class Image(models.Model):
    image = models.ImageField(blank=True,upload_to='media')
    image_name = models.CharField(max_length=50)
    image_desc = models.TextField(max_length=525)
    image_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    image_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Location(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)