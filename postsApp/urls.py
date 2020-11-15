from django.urls import path, include
from . import views

urlpatterns = [
    path('add-new/', views.new_post, name='new'),
    path('gallery/', views.gallery, name='gallery'),
]