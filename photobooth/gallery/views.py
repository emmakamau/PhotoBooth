from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def travel(request):
    travel_images = Image.objects.all()

    context={
        'travel_images':travel_images
    }
    return render(request,'category/travel.html',context=context)