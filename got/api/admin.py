from django.contrib import admin
from .models import Perso, Maison, Lieu, Continent

class PersoAdmin (admin.ModelAdmin):
    list_display=["complet_nom", "geniteur", "genitrice", "enfants_tag"]
    
    #Non fonctionel
    def complet_nom(self, obj):
        nom=obj.nom
        maison=obj.maison
        surnom=f'({obj.surnom})'
        
        if obj.surnom is not None:
            surnom=f'\"{obj.surnom}\"'
        else:
           surnom=""  
                  
        if obj.nombatard:
            nombatard=f'{obj.nombatard}, bâtard'
        else:
            nombatard=""
            
        try:
            obj.maisonnaissance.nommaison
            maisonnaissance=f"({obj.maisonnaissance.nommaison})"
        except:
            maisonnaissance="" 
               
        return (f'{nom} {surnom} {nombatard} {maison} {maisonnaissance}')
    
    def enfants_tag(self, obj):
           
        return ",\n".join([f'{e.nom} {e.maison.nommaison}' for e in obj.enfants.all()])            

admin.site.register(Perso, PersoAdmin)
admin.site.register(Maison)
admin.site.register(Lieu)
admin.site.register(Continent)
# Register your models here.
