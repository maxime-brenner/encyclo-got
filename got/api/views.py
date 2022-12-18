from django.shortcuts import render
from .serializers import PersoSerializer
from rest_framework import viewsets
from .models import Perso

class PersoView (viewsets.ModelViewSet):
    serializer_class = PersoSerializer
    queryset = Perso.objects.all()

# Create your views here.
