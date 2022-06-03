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