from django.test import TestCase
from .models import *

# Create your tests here.
class TestCategory(TestCase):
    def setUp(self) -> None:
        self.example_category = Category(name="New Category")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.example_category, Category))

class TestLocations(TestCase):
    def setUp(self) -> None:
        self.example_location = Location(name="Nairobi")

    def test_location_instance(self):
        self.assertTrue(isinstance(self.example_location, Location))

class TestImage(TestCase):
    def setUp(self) -> None:
        self.example_category = Category(name="New Category")
        self.example_category.save()

        self.example_location = Location(name="Nairobi")
        self.example_location.save()

        self.example_image = Image(image="../media/cow.jpeg",image_name="test_image",image_desc="This is a test for the Image model",
                                    image_location=self.example_location, image_category=self.example_category,
                                    )

    def tearDown(self) -> None:
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.example_image, Image))