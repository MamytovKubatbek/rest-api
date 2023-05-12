from rest_framework import serializers
from .models import *

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'






