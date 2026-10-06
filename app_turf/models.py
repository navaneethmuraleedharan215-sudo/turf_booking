from django.db import models

# Create your models here.
class Turf(models.Model):
    team_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    date=models.DateField(null=True)
    duration=models.IntegerField()
    fee=models.IntegerField()
    
