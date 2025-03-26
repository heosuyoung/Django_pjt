from django.db import models


# Create your models here.
class Board(models.Model):
    # 제목은 글자 제한을 20글자
    # 왜 20글자 제한?-> 게시글 제목이 너무 길어지면 페이지 다 잡아먹음
    title = models.CharField(max_length=20)
    # 게시글 내용(글자 제한x)
    content = models.TextField()
    # auto_now랑  auto_now_add차이
    # auto_now_add:객체가 처음 생성될때 시간
    create_at = models.DateTimeField(auto_now_add=True)
    # auto_now:객체가 저장 될 떄의 현재 시간
    updated_at = models.DateTimeField(auto_now=True)
    # 수동 입력 시간
    time_at = models.DateTimeField(null=True, blank=True)
