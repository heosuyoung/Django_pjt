# finlife/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),  # ✅ 추가!
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('deposit-products/top-rate/', views.top_rate),
    path('dummy-data/', views.generate_dummy_data),


]
