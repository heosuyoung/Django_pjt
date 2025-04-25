# mypjt/urls.py
from django.contrib import admin
from django.urls import path, include  # ← include 꼭 있어야 함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finlife/', include('finlife.urls')),  # ← 이거 추가해야 함
]
