from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render 

def home_view(request):
	return render(request, "index.html", {})

# Create your views here.
