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


"""
ORM 
DB는 SQL커리로 조작
Django는 python
:python 코드를 SQL쿼리로 변환해주는 도구
왜 ORM을 쓸까?
우리 사용하는 Django는 python DB는 SQL

QuerySet API
:이 구문을 사용하면 DB에 데이터를 접근하고, 조작(CRUD)할 수 있다.
ex) Article.objects.all()

create(객체 생성)
1. 첫번쨰 방법

article = Board()
article.title= 'first'
article.content = 'hello'
article.save()

2. 두번쨰 방법

article = Board(title = 'second', content ='hi')
article.save()

3. 세번쨰 방법

Board.objects.create(title = 'third', content='byebye')

#Q)우리는 객체를 생성할 떄 1번, 2번, 3번 방법
몇번 방법을 지양해야할까? 3번
객체를 지양하기 전에 데이터를 검증하고 그 다음에 save()
검증단계: 유효성 검사(valid check)


read(조회)

1.전체 조회
Board.objects.all()

2.특정 조건으로 데이터 조회 (filter)

Board.objects.filter(title = 'first')  이거있냐
Board.objects.filter(content__contains='he') 내용에 이게 포함 되냐
Board.objects.filter(title__startswith='f') 이걸로 시작하냐

조회한 객체가 없을 경우 예외 발생x

3. 단일 데이터 조회(get)

Board.objects.get(pk=1)
Board.objects.get(title='first')

없는 데이터 조회
Board.objects.get(title='fir')
->오류가 발생

조회한 객체가 없을 경우 예외 발생o
->고유성을 보장함
조회하는 객체가 2개 이상이다. 예외 발생함

->filter랑 get이랑 아주 큰 차이

update(수정)
article = Board.objects.get(pk=1)
article.title = 'first1'
article.save()

delete(삭제)

article = Board.objects.get(pk=1)
article.delete()

만약 새로운 객체를 생성하면 pk=1로 생성x pk=4로 생성된다.





"""
