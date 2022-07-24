from rest_framework import serializers
from .models import State, BigCity, SmallCity

class SmallCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SmallCity
        fields = ['name', 'big_city', 'big_city__state', 'big_city__state__name']

class ListSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmallCity
        fields = ['name']

class BigCitySerializer(serializers.ModelSerializer):
    small_cities = ListSmallSerializer(many=True)

    class Meta:
        model = BigCity
        fields = ['name', 'small_cities', 'state__name']

class ListBigCitySerializer(serializers.ModelSerializer):
    small_cities = ListSmallSerializer(many=True)

    class Meta:
        model = BigCity
        fields = ['name', 'small_cities']

class StateSerializer(serializers.ModelSerializer):
    big_cities = ListBigCitySerializer(many=True)

    class Meta:
        model = State
        fields = ['name', 'big_cities']