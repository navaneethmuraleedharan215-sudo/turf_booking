from rest_framework import serializers

class BookingSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    team_name=serializers.CharField(max_length=200)
    phone=serializers.IntegerField()
    date=serializers.DateField()
    time=serializers.TimeField()
    duration=serializers.IntegerField
    fee=serializers.IntegerField()
