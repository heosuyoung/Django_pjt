import requests
from django.http import JsonResponse
from django.conf import settings
from .models import DepositProducts, DepositOptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepositProductsSerializer
from .models import DepositProducts
from .models import DepositOptions
from .serializers import DepositOptionsSerializer
import random
import string
from rest_framework.decorators import api_view

def save_deposit_products(request):
    api_url = f"https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
        "auth": settings.API_KEY,
        "topFinGrpNo": "020000",  # 은행
        "pageNo": 1
    }

    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        return JsonResponse({"error": "API 요청 실패"}, status=500)

    data = response.json()
    base_list = data.get("result", {}).get("baseList", [])
    option_list = data.get("result", {}).get("optionList", [])

    # 1. 상품 목록 저장
    for item in base_list:
        product, _ = DepositProducts.objects.get_or_create(
            fin_prdt_cd=item.get("fin_prdt_cd"),
            defaults={
                "kor_co_nm": item.get("kor_co_nm"),
                "fin_prdt_nm": item.get("fin_prdt_nm"),
                "etc_note": item.get("etc_note"),
                "join_deny": int(item.get("join_deny")),
                "join_member": item.get("join_member"),
                "join_way": item.get("join_way"),
                "spcl_cnd": item.get("spcl_cnd"),
            }
        )

    # 2. 옵션 목록 저장
    for item in option_list:
        try:
            product = DepositProducts.objects.get(fin_prdt_cd=item.get("fin_prdt_cd"))
            DepositOptions.objects.create(
                product=product,
                fin_prdt_cd=item.get("fin_prdt_cd"),
                intr_rate_type_nm=item.get("intr_rate_type_nm"),
                intr_rate=float(item.get("intr_rate") or -1),
                intr_rate2=float(item.get("intr_rate2") or -1),
                save_trm=int(item.get("save_trm")),
            )
        except DepositProducts.DoesNotExist:
            continue  # 매칭 안 되면 무시

    return JsonResponse({"message": "저장 완료!"})

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    best_option = DepositOptions.objects.order_by('-intr_rate2').first()

    if not best_option:
        return Response({'message': '데이터가 없습니다.'}, status=404)

    product = best_option.product
    options = DepositOptions.objects.filter(product=product)

    product_serializer = DepositProductsSerializer(product)
    option_serializer = DepositOptionsSerializer(options, many=True)

    return Response({
        'product': product_serializer.data,
        'options': option_serializer.data,
    })


@api_view(['GET'])
def generate_dummy_data(request):
    dummy_data = []

    for _ in range(10):
        fin_prdt_cd = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        item = {
            "fin_prdt_cd": fin_prdt_cd,
            "kor_co_nm": random.choice(["가상은행", "미래은행", "AI금고"]),
            "fin_prdt_nm": random.choice(["슈퍼정기예금", "하이세이브", "드림플러스"]),
            "etc_note": "가입조건 없음. 자유입출금 가능.",
            "join_deny": 1,
            "join_member": "개인",
            "join_way": "인터넷, 스마트폰",
            "spcl_cnd": "우대금리 조건 없음"
        }
        dummy_data.append(item)

    return Response(dummy_data)
