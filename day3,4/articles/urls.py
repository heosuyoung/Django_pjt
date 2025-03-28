from django.urls import path

from . import views

"""
{% url namespace.name &}
app_name = 'namespace'
"""
app_name = "articles"

urlpatterns = [
    # 전체 게시글 조회
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    # create
    # 랜더링(생성 페이지를 보여줄거다)
    path("new/", views.new, name="new"),
    # 리다이렉트(생성 버튼을 눌렀을때 게시글이 생성)
    path("create/", views.create, name="create"),
    # 단일 게시글 조회--->ㅇ딛ㅅㄷ
    # variable routing
    path("<int:pk>/delete", views.delete, name="delete"),
    # update
    # 단일 게시글 조회 후 수정
    # variable routing
    # 페이지 렌더링
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
]
