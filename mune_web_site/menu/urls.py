from django.urls import path
from .views import CategoryViewSet, MenuItemViewSet

urlpatterns = [

    path(
        'categories/',
        CategoryViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='category_list'
    ),
    path(
        'categories/<int:pk>/',
        CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='category_detail'
    ),

    path(
        'menu-items/',
        MenuItemViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='menuitem_list'
    ),
    path(
        'menu-items/<int:pk>/',
        MenuItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='menuitem_detail'
    ),
]
