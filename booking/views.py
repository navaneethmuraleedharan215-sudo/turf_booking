from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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
        serializer_instance=BookingSerializer
    
