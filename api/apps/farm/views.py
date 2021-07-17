from django.shortcuts import render
from .models import Farm, Farmer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import FarmSerializer, FarmerSerializer


# Create your views here.
class FarmViewSet(ModelViewSet):
    serializer_class = FarmSerializer

    def get_queryset(self):
        return Farm.objects.all()


class FarmerViewSet(ModelViewSet):
    serializer_class = FarmerSerializer

    queryset = Farmer.objects.all()
