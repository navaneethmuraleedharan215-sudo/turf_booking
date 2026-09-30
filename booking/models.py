from django.db import models

from app_turf.models import Turf

# Create your models here.

class Slot(models.Model):
    team_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    Time=models.TimeField(editable=False,null=True)
    date=models.DateField()
    duration=models.IntegerField()