from django.urls import path
from .views import CategoryViewSet, MenuItemListViewSet,MenuItemDetailViewSet

urlpatterns = [

    path('categories/',CategoryViewSet.as_view(),name='category_list'),
    path('categories/<int:pk>/',CategoryViewSet.as_view(),name='category_detail'),
    path('menu-items/',MenuItemListViewSet.as_view(),name='menuitem_list'),
    path('menu-items/<int:pk>/',MenuItemDetailViewSet.as_view(),name='menuitem_detail'),

]
