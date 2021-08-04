# returns any model object in a json response 
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%m/%d/%Y %H:%M:%S')
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'in_stock', 'created_at']