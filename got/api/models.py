from django.db import models
from django.db.models import CharField, ManyToManyField, OneToOneField, ForeignKey,BooleanField, IntegerField, CASCADE

class Perso (models.Model):

    nom = CharField(("Nom"), max_length=50, blank=True, unique=False)
    surnom = CharField(("Surnom"), max_length=50, null=True, blank=True)
    maison = ForeignKey("api.Maison", related_name="Maison d\'appartenance+", blank=True, on_delete=CASCADE, null=True)
    maisonnaissance = ForeignKey("api.Maison", related_name="Maison de naissance+", verbose_name="Maison de naissance", blank=True, on_delete=CASCADE, null=True)
    batard = BooleanField("Batard", blank=True)
    nombatard = CharField(("Nom de Batard"), max_length=50, blank=True)
    geniteur = ForeignKey('self', related_name="Père", verbose_name="Père",on_delete=CASCADE, blank=True, null=True)
    genitrice = ForeignKey('self', related_name="Mère", verbose_name="Mère", on_delete=CASCADE, blank=True, null=True)
    epoux = ManyToManyField('self', blank=True)
    generation = IntegerField(("Génération"), null=True)
    isnoble = BooleanField(default=True)
    description = CharField("description", max_length=255, blank=True)
    deces = models.CharField(("Mort"), max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.nom}'

    class Meta:
        verbose_name = ("Perso ")
        verbose_name_plural = ("Perso s")


    def get_absolute_url(self):
        return reverse("Perso _detail", kwargs={"pk": self.pk})


class Maison (models.Model):
    
    nommaison = CharField(("Nom de la Maison"), max_length=50, unique=True)
    suzerain = ManyToManyField("self", blank=True)
    banneret = ManyToManyField("self", blank=True)
    membre = ManyToManyField("api.Perso", related_name="Membres",verbose_name=("Membres"), blank=True)
    fief = ForeignKey(("api.Lieu"), related_name="Fief", null=True, blank=True, on_delete=CASCADE)
    
    class Meta:
        verbose_name = ("Maison")
        verbose_name_plural = ("Maisons")
        
    def __str__(self):
        return self.nommaison

    def get_absolute_url(self):
        return reverse("Maison _detail", kwargs={"pk": self.pk})
    
class Lieu (models.Model):
    
    nom = CharField(("Nom"), max_length=50)
    continent = ForeignKey("api.Continent", related_name="Continent", null=True, on_delete=CASCADE)
    
    def __str__(self):
        return self.nom
    
    
    
class Continent (models.Model):
    
    nom = CharField(("Nom"), max_length=50)
    lieu = ManyToManyField("api.Lieu", related_name="Lieu", blank=True)
    
    def __str__(self):
        return self.nom
    


