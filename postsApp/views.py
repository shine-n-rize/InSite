from django.shortcuts import render
from .models import Post

posts = [
    {
        'user': 'v_shh',
        'title': 'First',
        'description': 'My first post',
        'date_posted': '12 Nov, 2020',
    },
    {
        'user': 'D',
        'title': 'Second',
        'description': 'My second post',
        'date_posted': '14 Nov, 2020',
    },
    {
        'user': 'mia',
        'title': 'Third',
        'description': 'My third post',
        'date_posted': '16 Nov, 2020',
    },
]

def new_post(request):
    return render(request, 'postsApp/new_post.html')

def gallery(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'postsApp/gallery.html', context)