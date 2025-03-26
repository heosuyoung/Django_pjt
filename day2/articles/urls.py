from django.contrib import admin
from django.urls import path

# .은 현재 디렉토리
from . import views

# url namespace
# 앱이 여러개라면, 다른앱과 혼동하지 않기 위해 namespace지정
app_name = "articles"

# href = 'https://127.0.0.1:8000/articles/index/'
# url named pattern
# {% url articles:index %}

urlpatterns = [
    path("", views.index, name="index"),
    path("dinner/", views.dinner, name="dinner"),
    path("search/", views.search, name="search"),
    path("throw/", views.throw, name="throw"),
    path("catch/", views.catch, name="catch"),
    # <데이터타입:변수명> : variable routing -> why 사용?
    # url의 뒤의 숫자가 바뀔때마다 path를 여러개 작성? xx
    # 하나의 view로 처리하기 위해 사용용
    path("<int:number>/", views.detail, name="detail"),
]
