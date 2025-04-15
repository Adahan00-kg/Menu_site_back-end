from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class MainTitleListAPIView(generics.ListAPIView):
    queryset = MainTitle.objects.all()
    serializer_class = MainTitleSerializer


class MiddleTitleTextAPIView(generics.ListAPIView):
    queryset = MiddleTitleText.objects.all()
    serializer_class = MiddleTitleTextSerializer


class MiddleSecondAPIView(generics.ListAPIView):
    queryset = MiddleSecondText.objects.all()
    serializer_class = MiddleSecondSerializer


class MenuTitleAPIView(generics.ListAPIView):
    queryset = MenuTitle.objects.all()
    serializer_class = MenuTitleSerializer


class AboutOurAPIView(generics.ListAPIView):
    queryset = AboutOur.objects.all()
    serializer_class = AboutOurSerializer


