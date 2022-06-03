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

    def test_save_image(self):
        self.example_image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) == 1)
    
    def test_delete_image(self):
        self.example_image.save_image()
        self.example_image.delete_image(self.example_image.id)
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update_image(self):
        self.example_image.save_image()

        self.updated_category = Category(name="Food")
        self.updated_category.save()
        self.updated_location = Location(name="Nyeri")
        self.updated_location.save()

        self.example_image.update_image(
            new_image="../media/cow.jpeg",
            new_image_name="New_Img",
            new_image_desc="Test image update",
            new_image_location=self.updated_location,
            new_image_category=self.updated_category,
        )

        updated_image = self.example_image

        self.assertEqual(self.example_image, updated_image)

    def test_get_image_by_id(self):
        self.example_image.save_image()
        image = self.example_image.get_image_by_id(self.example_image.id)
        self.assertEqual(self.example_image, image)

    def test_get_images_by_category(self):
        self.example_image.save_image()
        searched = self.example_image.get_image_by_category("New Category")
        self.assertTrue(len(searched) == 1)

    def test_get_images_by_location(self):
        self.example_image.save_image()
        searched = self.example_image.get_image_by_location("Nairobi")
        self.assertTrue(len(searched) == 1)