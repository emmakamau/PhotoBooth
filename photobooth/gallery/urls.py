from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name = 'homepage'),
    path('gallery/',views.gallery,name = 'gallery'),
    path('search/', views.search_by_category, name='search')
]