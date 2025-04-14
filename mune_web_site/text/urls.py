from django.urls import path
from .views import *


urlpatterns = [
    path('main_text/',MainTitleListAPIView.as_view(),name = 'main_text'),
    path('middle_text/',MiddleTitleTextAPIView.as_view(),name = 'middle_text'),
    path('middle_second_text',MiddleSecondAPIView.as_view(),name = 'middle_second_text'),
    path('menu_text',MenuTitleAPIView.as_view(),name = 'menu_text'),
    path('about',AboutOurAPIView.as_view(),name = 'about_our'),

]

