from rest_framework import serializers
from .models import *

class MainTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTitle
        fields = '__all__'



class MiddleTitleTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleTitleText
        fields = '__all__'



class MiddleSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleSecondText
        fields = '__all__'



class MenuTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTitle
        fields = '__all__'


class AboutOurSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutOur
        fields = '__all__'