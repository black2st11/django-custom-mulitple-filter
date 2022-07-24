from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from region.models import State, BigCity, SmallCity
from faker import Faker
import random
from django.db.models.query import QuerySet
@pytest.fixture()
def create_test_db(db):
    fake = Faker('ko_KR')
    for i in range(1000):
        address = fake.address()
        address_list = address.split(' ')
        state_name, big_city_name, small_city_name = address_list[0], address_list[1], address_list[2]
        state = State.objects.get_or_create(name=state_name)
        big_city = BigCity.objects.get_or_create(state_id=state[0].id, name=big_city_name)
        small_city = SmallCity.objects.get_or_create(big_city_id=big_city[0].id, name=small_city_name)

def randomnized(queryset, times, key):
    return [getattr(item, key) for item in  random.choices(queryset, k=times)]



def find_data(queryset, fields, key, datas):
    if not fields:
        for model_object in queryset:
            if getattr(model_object, key) in datas:
                return True
        return False
    
    field = fields[0]
    for model_object in queryset:
        new_queryset = getattr(model_object, field).all()
        if not find_data(new_queryset, fields[1:], key, datas):
            return False
    return True


@pytest.mark.django_db
class TestFilter:
    pytestmark = pytest.mark.django_db
    def test_state_filter_by_small_city(self, create_test_db):
        small_cities = SmallCity.objects.all()
        small_city_names = randomnized(small_cities, 1, 'name')
        data = {"small_cities" : small_city_names}
        client = APIClient()
        res = client.get('/state/', data)
        states = res.data

        assert res