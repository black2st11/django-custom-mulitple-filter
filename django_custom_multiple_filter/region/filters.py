from random import choices
from django_filters import rest_framework as filters
from custom_filters.filters import MultipleFilter
from .models import BigCity, SmallCity, State

class StateFilter(filters.FilterSet):
    big_cities = MultipleFilter(field_name='big_cities__name', coerce=str)
    small_cities = MultipleFilter(field_name='big_cities__small_cities__name', coerce=str)

    class Meta:
        model = State
        fields = ['big_cities', 'small_cities']


class BigCityFilter(filters.FilterSet):
    states = MultipleFilter(field_name='state__name', coerce=str)
    small_cities = MultipleFilter(field_name='small_cities__name', coerce=str)

    class Meta:
        model = BigCity
        fields = ['states', 'small_cities']


class SmallCityFilter(filters.FilterSet):
    states = MultipleFilter(field_name='big_city__state__name', coerce=str)
    big_cities = MultipleFilter(field_name='big_city__name', coerce=str)

    class Meta:
        model = SmallCity
        fields = ['states', 'big_cities']