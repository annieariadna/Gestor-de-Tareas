from django.urls import path
from . import views 
urlpatterns = [
    path('layout/',views.layout, name='layout'),
    path('indexal/',views.index, name='index'),
]