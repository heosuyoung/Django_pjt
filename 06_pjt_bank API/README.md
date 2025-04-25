# 06_PJT 금융상품정보 API Server

## 프로젝트 개요
- 금융감독원 정기예금 API 데이터를 수집하고 가공하여 제공하는 Django REST API 서버
- 정기예금 상품 및 옵션 목록 조회, 금리 기준 정렬, 더미데이터 생성 기능 포함

## 기능 요약
1. `/finlife/save-deposit-products/` - API에서 상품/옵션 정보 수집 및 DB 저장
2. `/finlife/deposit-products/` - 상품 목록 조회 (GET) / 수동 등록 (POST)
3. `/finlife/deposit-product-options/<fin_prdt_cd>/` - 특정 상품의 옵션 리스트 조회
4. `/finlife/deposit-products/top-rate/` - 최고 금리 상품 및 옵션 정보 조회
5. `/finlife/dummy-data/` - 더미 데이터 JSON 형식으로 생성

## 환경 변수
- `.env` 파일에 다음 항목을 포함해야 함:
```
API_KEY="여기에_금융감독원_API키_입력"
```

## 실행 방법
```bash
pip install -r requirements.txt
python manage.py runserver
```

## Postman 테스트 활용법
- 루트에 포함된 `06_pjt_postman_collection.json` 파일을 이용해 전체 기능 테스트 가능
- 사용 방법:
  1. Postman 실행
  2. Import → File 선택 → `06_pjt_postman_collection.json` 선택
  3. 6개의 요청이 세트로 구성되어 있음 (GET/POST 요청 확인)

## 프로젝트 폴더 구조 예시
```
06_PJT/
├── finlife/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── mypjt/
│   ├── settings.py
│   └── urls.py
├── .env
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
├── 06_pjt_postman_collection.json
```

---

