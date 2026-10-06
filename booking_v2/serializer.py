from rest_framework import serializers
from booking_v2.models import booking
from django.contrib.auth.models import User


class bookingserializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields="__all__"

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]