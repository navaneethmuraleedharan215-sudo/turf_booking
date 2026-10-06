from django.db import models

from app_turf.models import Turf

# Create your models here.

class Slot(models.Model):
    team_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    date=models.DateField(null=True)
    time=models.TimeField()
    duration=models.IntegerField()
    fee=models.IntegerField()