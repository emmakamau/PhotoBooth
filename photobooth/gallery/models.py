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

    def __str__(self):
        return self.image_name

    def save_image(self):
        '''
        Method that saves an image
        '''
        self.save()

    def update_image(self, new_image, new_image_name, new_image_desc, new_image_location, new_image_category):
        '''
        Update Image
        '''
        self.image = new_image
        self.image_name = new_image_name
        self.image_desc = new_image_desc
        self.image_location = new_image_location
        self.image_category = new_image_category

    @classmethod
    def delete_image(cls,id):
        '''
        Delete image from database
        '''
        image = Image.objects.get(id=id)
        image.delete()

    @classmethod
    def get_image_by_id(cls,id):
        '''
        Get specific image by id
        '''
        image = Image.objects.get(id=id)
        return image

    @classmethod
    def get_image_by_category(cls,category):
        '''
        Method to search image based on category
        '''
        try:   
            category = Category.objects.get(name=category)
            category_list = Image.objects.filter(image_category=category.id)
            return category_list
        except Exception:
            return "No images found"

    @classmethod
    def get_image_by_location(cls,location):
        '''
        Method to search image based on category
        '''
        try:   
            location = Location.objects.get(name=location)
            location_list = Image.objects.filter(image_location=location.id)
            return location_list
        except Exception:
            return "No images found"

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name