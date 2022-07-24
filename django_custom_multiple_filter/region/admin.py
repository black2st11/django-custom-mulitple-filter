from django.contrib import admin
from .models import State, BigCity, SmallCity


admin.site.register(State)
admin.site.register(BigCity)
admin.site.register(SmallCity)