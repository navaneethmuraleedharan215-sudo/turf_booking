from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from app_turf.serializer import UserSerializer,turfSerializer
from app_turf.models import Turf




# Create your views here.

class UserAdminCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            User.objects.create_superuser(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

class TurfListCreateView(APIView):
    def get(self,request):
        qs=Turf.objects.all()
        serializer_instance=turfSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=turfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Turf.objects.create(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

class TurfRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs=Turf.objects.get(id=pk)
        serializer_instance=turfSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=turfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Turf.objects.create(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)        