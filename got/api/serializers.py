from rest_framework import serializers
from .models import Perso, Maison, Lieu, Continent

class PersoSerializer(serializers.ModelSerializer):
    
    maison_nom=serializers.SerializerMethodField()
    maisonnaissance_nom = serializers.SerializerMethodField()
    
    
    def get_maison_nom(self, obj):
        if obj.maison:
            return obj.maison.nommaison
        else:
            return None
        
    def get_maisonnaissance_nom(self, obj):
        if obj.maisonnaissance:
            return obj.maisonnaissance.nommaison
        else:
            return None
        
    
    class Meta:
        model = Perso
        #fields = [field.name for field in Perso._meta.get_fields()]
        fields = ["id", "nom", "maison", "maison_nom", "maisonnaissance_nom", "generation"]
        
class LieuSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Lieu
        fields = ["nom"]
        
        
        
    