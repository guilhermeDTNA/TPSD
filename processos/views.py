from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import GeralSerializer, ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class GeralViewSet(viewsets.ModelViewSet):
    queryset = Geral.objects.all()
    serializer_class = GeralSerializer