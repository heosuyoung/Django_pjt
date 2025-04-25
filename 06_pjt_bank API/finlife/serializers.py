from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ['product']

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
