from django.contrib import admin

# Register your models here.

# models.py로 부터 Board클래스
from .models import Board

# admin site에 등록
admin.site.register(Board)
