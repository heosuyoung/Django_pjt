from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from boards.models import Board, Comment


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # ✅ backend 명시 추가
            auth_login(request, user)  # ✅ 에러 해결됨
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('boards:index')


@login_required
def profile(request, pk):
    profile_user = get_object_or_404(User, pk=pk)
    boards = Board.objects.filter(author=profile_user)
    comments = Comment.objects.filter(author=profile_user)
    is_following = request.user in profile_user.followers.all()

    context = {
        'profile_user': profile_user,
        'boards': boards,
        'comments': comments,
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, pk):
    profile_user = get_object_or_404(User, pk=pk)
    if request.user != profile_user:
        if request.user in profile_user.followers.all():
            profile_user.followers.remove(request.user)
        else:
            profile_user.followers.add(request.user)
    return redirect('accounts:profile', pk=pk)
