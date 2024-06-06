from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts, LoanOptions, LoanProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class OptioninProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositOptions
            fields = '__all__'
    depositoptions_set = OptioninProductSerializer(read_only=True,many=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'
    
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)
        
class SavingProductsSerializer(serializers.ModelSerializer):
    class OptioninProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingOptions
            fields = '__all__'
    savingoptions_set = OptioninProductSerializer(read_only=True,many=True)
    class Meta:
        model = SavingProducts
        fields = '__all__'
    
class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)
        
class LoanProductsSerializer(serializers.ModelSerializer):
    class OptioninProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = LoanOptions
            fields = '__all__'
    loanoptions_set = OptioninProductSerializer(read_only=True,many=True)
    class Meta:
        model = LoanProducts
        fields = '__all__'

class LoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanOptions
        fields = '__all__'
        read_only_fields = ('product',)