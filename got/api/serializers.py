from rest_framework import serializers
from .models import Perso, Maison, Lieu, Continent

class PersoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perso
        fields = [field.name for field in Perso._meta.get_fields()]