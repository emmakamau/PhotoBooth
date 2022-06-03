from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def gallery(request):
    gallery = Image.objects.all()
    context={
        'gallery':gallery
    }
    return render(request,'category/gallery.html',context=context)
