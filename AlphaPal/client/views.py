from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, User_Profile_form
from .decorators import allowed_users

# Create your views here.
@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'client/profile.html', context)


@login_required(login_url='login')
def userProfile(request, pk):
    prof = Profile.objects.get(id=pk)
    context = {'prof': prof}
    return render(request, 'client/user-profile.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.warning(request, 'Username or Password incorrect!')
    else:
        form = AuthenticationForm()

    return render(request, 'client/login_register.html', context={'form': form})


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'client/login_register.html', context)


def user_profile_update(request, pk):
    order = Profile.objects.get(id=pk)
    form = User_Profile_form(instance=order)

    if request.method == 'POST':
        form = User_Profile_form(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'client/user_profile_update.html', context)