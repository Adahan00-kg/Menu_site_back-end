from django.urls import path
from .views import CategoryListViewSet, MenuItemListViewSet, MenuItemDetailViewSet, CategoryDetailViewSet

urlpatterns = [

    path('categories/',CategoryListViewSet.as_view(),name='category_list'),
    path('categories/<int:pk>/',CategoryDetailViewSet.as_view(),name='category_detail'),
    path('menu-items/',MenuItemListViewSet.as_view(),name='menuitem_list'),
    path('menu-items/<int:pk>/',MenuItemDetailViewSet.as_view(),name='menuitem_detail'),

]
