from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SaveProducts, SaveOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = DepositProducts
        fields = '__all__'
        
        
class DepositOptionsSerializer(serializers.ModelSerializer):
    fin_prdt_nm = serializers.CharField(source='product.fin_prdt_nm', read_only=True)
    class Meta():
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class SaveProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = SaveProducts
        fields = '__all__'

class SaveOptionsSerializer(serializers.ModelSerializer):
    fin_prdt_nm = serializers.CharField(source='product.fin_prdt_nm', read_only=True)
    class Meta():
        model = SaveOptions
        fields = '__all__'
        read_only_fields = ('product',)