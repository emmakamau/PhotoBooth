from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name = 'homepage'),
    path('travel/',views.travel,name = 'travel'),
    path('food/',views.food,name = 'food'),
    path('potraits/',views.potraits,name = 'potraits')
]