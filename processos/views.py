from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import GeralSerializer


class GeralViewSet(viewsets.ModelViewSet):
    queryset = Geral.objects.all()
    serializer_class = GeralSerializer