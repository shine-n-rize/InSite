from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView

from .forms import (
    UserRegisterForm, 
    UserUpdateForm, 
    ProfileUpdateForm
)
from .models import Profile



def home(request):
    return render(request, 'usersApp/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!<br>You are eligible for Login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersApp/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'usersApp/profile.html', context)


def search(request):
    qur = request.GET.get('search').lower()
    # profiles = Profile.objects.filter(user__icontains = qur)
    profiles = [item for item in Profile.objects.all() if qur in item.user.username.lower()]
    return render(request, 'usersApp/search.html', {'profiles': profiles})


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'usersApp/search_profile.html'