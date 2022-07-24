from django.core.management.base import BaseCommand, CommandError
from region.models import State, BigCity, SmallCity
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker('ko_KR')
        for i in range(1000):
            address = fake.address()
            address_list = address.split(' ')
            state_name, big_city_name, small_city_name = address_list[0], address_list[1], address_list[2]
            state = State.objects.get_or_create(name=state_name)
            big_city = BigCity.objects.get_or_create(state_id=state[0].id, name=big_city_name)
            small_city = SmallCity.objects.get_or_create(big_city_id=big_city[0].id, name=small_city_name)