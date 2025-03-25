from django.shortcuts import render


# Create your views here.
def index(request):

    context = {"name": "bogum", "number": 1}

    return render(request, "articles/index.html", context)


import random


def dinner(request):
    foods = ["족발", "보쌈", "치킨", "피자"]
    picked = random.choice(foods)
    context = {"foods": foods, "picked": picked}

    return render(request, "articles/dinner.html", context)


def search(request):
    return render(request, "articles/search.html")


def throw(request):
    return render(request, "articles/throw.html")


def catch(request):
    # name 'throw'
    # GET:GET방식
    # .get: 딕서녀리의 Value
    # 'throw':딕셔너리의 key

    text = request.GET.get("throw")
    context = {"text": text}
    return render(request, "articles/catch.html", context)
