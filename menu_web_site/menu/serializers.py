from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class MenuItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title','description','price','image','category_connect']



class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['extra_price','extra_name']


class MenuItemDetailSerializer(serializers.ModelSerializer):
    extra = ExtrasSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = ['title','description','price','image','category_connect','extra']
