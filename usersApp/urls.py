from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^profile/(?P<username>[\w.@+-]+)$', views.get_user_profile),
]
