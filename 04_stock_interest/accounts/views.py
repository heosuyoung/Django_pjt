from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from contentfetch.models import Stock
from django.shortcuts import get_object_or_404


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("stock_finder")  # 로그인 후 메인 페이지로
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("stock_finder")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("stock_finder")


@login_required
def profile_view(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, "accounts/profile.html", {"stocks": stocks})


@login_required
def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id, user=request.user)
    stock.delete()
    return redirect("profile")


@login_required
def profile_view(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, "accounts/profile.html", {"stocks": stocks})
