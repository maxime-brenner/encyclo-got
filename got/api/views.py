from django.shortcuts import render
from .serializers import PersoSerializer, LieuSerializer
from rest_framework import viewsets
from .models import Perso, Lieu

class PersoView (viewsets.ModelViewSet):
    serializer_class = PersoSerializer
    queryset = Perso.objects.all()
    
class LieuView(viewsets.ModelViewSet):
    serializer_class = LieuSerializer
    queryset = Lieu.objects.all()

# Create your views here.
