from django.db import models

# 최상위 모델
class State(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

# 중간 모델
class BigCity(models.Model):
    state = models.ForeignKey('region.State', on_delete=models.DO_NOTHING, related_name='big_cities')
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

# 하위 모델
class SmallCity(models.Model):
    big_city = models.ForeignKey('region.BigCity', on_delete=models.DO_NOTHING, related_name='small_cities')
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']