from rest_framework import serializers
from app_turf.models import Turf

class UserSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

class turfSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    team_name=serializers.CharField(max_length=200)
    phone=serializers.IntegerField()
    date=serializers.DateField()
    duration=serializers.IntegerField
    fee=serializers.IntegerField()
    def validate(self,validated_data):
        fee=validated_data.get("fee")
        if fee<800:
            raise serializers.ValidationError("invalid fee,fee should be >800")
        else:
            return validated_data