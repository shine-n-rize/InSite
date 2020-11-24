from django.urls import path, include
from . import views
from usersApp.views import ProfileDetailView

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<int:pk>/profile', ProfileDetailView.as_view(), name='search-profile'),
]
