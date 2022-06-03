from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def gallery(request):
    gallery = Image.objects.all()
    category = Category.objects.all()
    context={
        'gallery':gallery,
        'category':category
    }
    return render(request,'category/gallery.html',context=context)

def search_by_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        search_image = Image.search_image(category)
        
        context={
            'search_image':search_image
        }
        return render(request,'category/search.html', context=context)
    return redirect('/')