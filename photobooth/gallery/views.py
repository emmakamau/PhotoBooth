from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def travel(request):
    travel_images = Image.objects.filter(image_category='0')

    context={
        'travel_images':travel_images
    }
    return render(request,'category/travel.html',context=context)

def food(request):
    food_images = Image.objects.filter(image_category='0')

    context={
        'food_images':food_images
    }
    return render(request,'category/food.html',context=context)

def potraits(request):
    potraits_images = Image.objects.filter(image_category='0')

    context={
        'potraits_images':potraits_images
    }
    return render(request,'category/potraits.html',context=context)