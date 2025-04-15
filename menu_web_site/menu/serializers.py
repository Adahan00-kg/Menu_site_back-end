from rest_framework import serializers
from .models import *



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class MenuItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','description','price','image','category_connect']


class CategoryDetailSerializer(serializers.ModelSerializer):
    items = MenuItemListSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','category_name','items']


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['id','extra_price','extra_name']


class MenuItemDetailSerializer(serializers.ModelSerializer):
    extra = ExtrasSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','description','price','image','category_connect','extra']


