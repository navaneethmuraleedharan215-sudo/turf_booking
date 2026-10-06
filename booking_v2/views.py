from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from booking_v2.serializer import SignupSerializer
from django.contrib.auth.models import User

class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_object=User.objects.create_user(**cleaned_data)
            serializer_instance=SignupSerializer(user_object)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

