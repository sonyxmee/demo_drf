from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    vin = models.CharField(unique=True, max_length=64, verbose_name='Vin', db_index=True)
    color = models.CharField(max_length=64, verbose_name='Color')
    brand = models.CharField(max_length=64, verbose_name='Brand')
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    type = models.IntegerField(choices=CAR_TYPES, verbose_name='Type')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
