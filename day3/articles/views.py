from django.shortcuts import render

# Create your views here.
from .models import Board


def index(request):
    # QuerySetAPI---> Read, 전체 데이터 조회 : Board.objects.all()
    articles = Board.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


