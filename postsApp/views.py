from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User



def new_post(request):
    return render(request, 'postsApp/new_post.html')


def gallery(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'postsApp/gallery.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'postsApp/gallery.html'     # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'postsApp/post_form.html'     # <app>/<model>_<viewtype>.html
    fields = ['post_image', 'title', 'description']
    success_url = '../gallery'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '../gallery'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False