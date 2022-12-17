from django.db import models
from django.db.models import CharField, ManyToManyField, OneToOneField, ForeignKey,BooleanField, CASCADE

class Perso (models.Model):

    nom = CharField(("Nom"), max_length=50, blank=True, unique=True)
    maison = ManyToManyField("api.Maison", related_name="Maison d\'appartenance+", blank=True)
    batard = BooleanField("Batard", blank=True)
    nombatard = CharField(("Batard"), max_length=50, blank=True)
    geniteur = ForeignKey('self', related_name="Père",on_delete=CASCADE, blank=True)
    genitrice = ForeignKey('self', related_name="Mère",on_delete=CASCADE, blank=True)
    epoux = ManyToManyField('self', blank=True)
    enfants = ManyToManyField('self', blank=True)
    isnoble = BooleanField(default=False)
    description = CharField("description", max_length=255, blank=True)
    deces = models.CharField(("Mort"), max_length=255, blank=True)

    class Meta:
        verbose_name = ("Perso ")
        verbose_name_plural = ("Perso s")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("Perso _detail", kwargs={"pk": self.pk})


class Maison (models.Model):
    
    nommaison = CharField(("Nom de la Maison"), max_length=50, unique=True)
    perso = ManyToManyField(Perso, related_name="Membres de la maison+",blank=True)
    suzerain = ManyToManyField("self", related_name="Suzerain Lige", blank=True)
    banneret = ManyToManyField("self", related_name="Bannerets", blank=True)
    membre = ManyToManyField(Perso, related_name="Bannerets",verbose_name=("Membres"), blank=True)
    
    class Meta:
        verbose_name = ("Maison")
        verbose_name_plural = ("Maisons")
        
    def __str__(self):
        return self.nommaison

    def get_absolute_url(self):
        return reverse("Maison _detail", kwargs={"pk": self.pk})
    


