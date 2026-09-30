from rest_framework import serializers
from .models import Product, PurchaseRelationship

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'isActive', 'imageUrl' ]

class PurchaseRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRelationship
        fields = ['id', 'source_product', 'target_product', 'weight']