from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from app_turf.models import Turf

from booking.models import Slot
from booking.serializer import BookingSerializer

# Create your views here.

class BookingListCreateView(APIView):
    def get(self,request):
        qs=Slot.objects.all()
        serializer_instance=BookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=BookingSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            turf=cleaned_data.get("turf")
            match_date=cleaned_data.get("match_date")
            new_token=0
            last_

    
