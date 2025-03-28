from django.shortcuts import render, redirect

# 현재 디렉토리의 models.py로 부터 Board 모델을 가져오겠다.
from .models import Article


def index(request):
    # QuerySetAPI ---> Read, 전체 데이터 조회 : Board.objects.all()
    articles = Article.objects.all()

    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)


def detail(request, pk):

    article = Article.objects.get(pk=pk)

    context = {"article": article}
    return render(request, "articles/detail.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    # post방식이 최고지만 get방식을 쓰는이유는
    # get방식에 비해 post 방식이 훨씬 복잡함 : ex) (csrf토큰) - (보안토큰)

    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article(title=title, content=content)
    # 데이터를 db에 함부로 저장하면 안됨
    # save하기 전에 유효성 검사
    article.save()

    # render,redirect차이
    # 우리가 사용자에게 새로운 페이지를 보여줄때 사용 render
    # 데이터 처리후(생성,수정,삭제) 다른 페이지로 이동할때 redirect
    return redirect("articles:detail", article.pk)


# articles = Board.objects.get(pk=pk)


# 단일 게시글 조회 후 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")


# 페이지 렌더링(게시글 조회)
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/edit.html", context)


# 페이지 리다이렉트 (create와 차이 : 기존에 있던 게시글을 변경)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get("title")
    article.content = request.POST.get("content")

    article.save()

    return redirect("articles:detail", article.pk)
