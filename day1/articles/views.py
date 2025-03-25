from django.shortcuts import render


# Create your views here.
def index(request):
    # 페이지를 렌더링하겠다. // 리다이렉트
    # articels앱의 index.html 페이지를 렌더링하겠다다
    return render(request, "articles/index.html")
