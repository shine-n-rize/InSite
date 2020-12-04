from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from postsApp.models import Post
from django.core.mail import send_mail
from .forms import contactformemail


def home_view(request):
    posts = Post.objects.all()
    if request.method == "GET":
        form = contactformemail()
    else:
        form = contactformemail(request.POST)
        if form.is_valid():
            frommail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, frommail, [
                      'swag.level.zero@gmail.com', frommail])
    return render(request, 'index.html', {'posts': posts, 'form': form})
