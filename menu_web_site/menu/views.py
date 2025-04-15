from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemListSerializer, CategoryListSerializer,MenuItemDetailSerializer,CategoryDetailSerializer


class CategoryListViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailViewSet(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class MenuItemListViewSet(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemListSerializer


class MenuItemDetailViewSet(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemDetailSerializer
