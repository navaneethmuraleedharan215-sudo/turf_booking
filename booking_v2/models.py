from django.db import models

from app_turf.models import Turf

# Create your models here.


class booking(models.Model):

    team_name=models.CharField(max_length=200)
    turf=models.ForeignKey(Turf,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    email=models.DateField()
    date=models.DateField()
    time=models.TimeField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    match_duration=models.DurationField()

    def __str__(self):
        return f"{self.team_name}-{self.turf}"
