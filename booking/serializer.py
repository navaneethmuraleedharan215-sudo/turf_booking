from rest_framework import serializers

class BookingSerializer(serializers.Serializer):
    team_name=serializers.CharField()
    phone=serializers.CharField()
    email=serializers.EmailField()
    time=serializers.TimeField(read_only=True)
    date=serializers.DateField()
    duration=serializers.IntegerField()
