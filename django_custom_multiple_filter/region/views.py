from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import State, BigCity, SmallCity
from .serializers import BigCitySerializer, SmallCitySerializer, StateSerializer
from .filters import BigCityFilter, SmallCityFilter, StateFilter


class BigCityView(ModelViewSet):
    queryset = BigCity.objects.all()
    serializer_class = BigCitySerializer
    filterset_class = BigCityFilter


class SmallCityView(ModelViewSet):
    queryset = SmallCity.objects.all()
    serializer_class = SmallCitySerializer
    filterset_class = SmallCityFilter


class StateView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filterset_class = StateFilter