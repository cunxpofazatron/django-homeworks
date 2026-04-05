from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'price', 'quantity']

class StockSerializer(serializers.ModelSerializer):
    products = StockProductSerializer(source='positions', many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products']

    def create(self, validated_data):
        products_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)

        for product in products_data:
            StockProduct.objects.create(stock=stock, **product)

        return stock

    def update(self, instance, validated_data):
        products_data = validated_data.pop('positions')

        instance.address = validated_data.get('address', instance.address)
        instance.save()

        instance.positions.all().delete()

        for product in products_data:
            StockProduct.objects.create(stock=instance, **product)

        return instance
