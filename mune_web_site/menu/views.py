from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemListSerializer, CategorySerializer,MenuItemDetailSerializer


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemListViewSet(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemListSerializer


class MenuItemDetailViewSet(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemDetailSerializer
