from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def homepage(request):
    category = Category.objects.all()
    context={
        'category':category
    }
    return render(request,'index.html',context=context)

def gallery(request):
    gallery = Image.objects.all()
    category = Category.objects.all()
    context={
        'gallery':gallery,
        'category':category
    }
    return render(request,'category/gallery.html',context=context)

def search_by_category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        category = request.POST.get('category')
        print(category)
        search_image = Image.get_image_by_category(category)
        
        context={
            'search_image':search_image,
            'category':category
        }
        return render(request,'category/search.html', context=context)
    return redirect('/')