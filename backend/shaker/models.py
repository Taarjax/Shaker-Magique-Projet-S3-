# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
# * Make sure each model has one field with primary_key = True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg
import os
import pprint


def upload_to(instance, filename):
    rel_path = os.path.join('cocktail', f'{instance.id}.jpg')
    path = os.path.join(settings.MEDIA_ROOT, rel_path)

    # Écraser l'image actuelle s'il y en a une
    if os.path.exists(path):
        os.remove(path)

    return rel_path


class Cocktail(models.Model):
    """Classe de liaison avec la table Cocktail
    """

    # Choix pour la catégorie
    # Ex. (VALEUR, REPRÉSENTATION HUMAINE)
    cat_choices = (
        ('A', 'Apéritif'),
        ('D', 'Digestif'),
        ('AD', 'Les deux')
    )

    id = models.AutoField(db_column='ID', primary_key=True)
    intitule = models.CharField(db_column='INTITULE', max_length=255)
    illustrationurl = models.ImageField(
        _("Image"), upload_to=upload_to, default='cocktail/default.jpg')
    categorie = models.CharField(db_column='CATEGORIE', max_length=255, choices=cat_choices)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    forcealc = models.IntegerField(db_column='FORCEALC', blank=True, null=True)
    ingredients = models.ManyToManyField("Ingredient", through="Contenir", through_fields=("idcocktail", "idingredient"))
    membres = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Propose", through_fields=("idcocktail", "idmembre"))

    @property
    def moyenne(self):
        return Noter.get_cached_avg(self.id)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calculer le cache des moyennes de tous les cocktails
        # dès l'initialisation du modèle
        Noter.cache_avg()

    def delete(self):
        """Supprimer l'instance et retirer du cache de moyenne
        """
        Noter.cached_moyenne.pop(self.id)
        super().delete()

    class Meta:
        managed = False        # Indique si Django peut gérer la structure de la table lui-même
        db_table = 'COCKTAIL'   # Nom de la table dans la BDD
        ordering = ('id',)      # Trier les instances par ID ascendant

    def __str__(self):
        """Représentation d'une instance\n
        Par exemple, permet d'afficher le nom du cocktail dans les listes déroulantes,
        du panel admin Django

        Returns: 
        string : Intitulé du cocktail
        """
        return self.intitule


class Contenir(models.Model):
    idcontenir = models.IntegerField(db_column='IDCONTENIR', primary_key=True)
    idcocktail = models.ForeignKey('COCKTAIL', models.DO_NOTHING, db_column='IDCOCKTAIL')
    idingredient = models.ForeignKey('INGREDIENT', models.DO_NOTHING, db_column='IDINGREDIENT')
    quantite = models.IntegerField(db_column='QUANTITE')
    unite = models.CharField(db_column='UNITE', max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONTENIR'
        unique_together = (('idcocktail', 'idingredient'),)


class Favori(models.Model):
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')
    idmembre = models.OneToOneField(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='IDMEMBRE', primary_key=True)

    class Meta:
        managed = False
        db_table = 'FAVORI'
        unique_together = (('idmembre', 'idcocktail'),)


class Ingredient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    intitule = models.CharField(db_column='INTITULE', max_length=255)
    degrealcool = models.IntegerField(db_column='DEGREALCOOL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INGREDIENT'

    def __str__(self):
        return self.intitule


class Noter(models.Model):
    idnoter = models.IntegerField(db_column='IDNOTER', primary_key=True)
    idmembre = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='IDMEMBRE')
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')
    note = models.IntegerField(db_column='NOTE')

    cached_moyenne = None  # Cache des moyennes de tous les cocktails

    @staticmethod
    def cache_avg():
        """Créer le cache des moyennes de tous les cocktails
        """
        if (Noter.cached_moyenne is None):
            Noter.cached_moyenne = {}
            instances = Noter.objects.values("idcocktail").annotate(moyenne=Avg("note"))

            for instance in instances:
                Noter.cached_moyenne[int(instance["idcocktail"])] = float(instance["moyenne"])

    @staticmethod
    def get_cached_avg(id):
        """Récupérer la moyenne d'un cocktail depuis le cache

        Args:
            id (int): ID du cocktail

        Returns:
            float: Moyenne du cocktail
        """
        return Noter.cached_moyenne.get(id)

    @staticmethod
    def update_cache_avg(id):
        """Mettre à jour le cache de la moyenne d'un cocktail

        Args:
            id (int): ID du cocktail
        """
        queryset = Noter.objects.filter(idcocktail=id).aggregate(moyenne=Avg("note"))["moyenne"]

        if (queryset is None):
            Noter.cached_moyenne.pop(id)
        else:
            Noter.cached_moyenne[id] = queryset

    @staticmethod
    def delete_cache_avg(id):
        """Supprimer un cocktail du cache des moyenne

        Args:
            id (int): ID du cocktail
        """
        Noter.cache_avg.pop(id)

    def delete(self):
        """Supprimer l'instance et mettre à jour le cache
        """
        super().delete()
        Noter.update_cache_avg(self.idcocktail.id)

    def save(self, **kwargs):
        """Créer l'instance et mettre à jour le cache
        """
        super().save(**kwargs)
        Noter.update_cache_avg(self.idcocktail.id)

    class Meta:
        managed = False
        db_table = 'NOTER'
        unique_together = (('idmembre', 'idcocktail'),)


class Preference(models.Model):
    idpreference = models.IntegerField(db_column="IDPREFERENCE", primary_key=True)
    idingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IDINGREDIENT')  # Field name made lowercase.
    idmembre = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='IDMEMBRE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PREFERENCE'
        unique_together = (('idmembre', 'idingredient'),)


class Propose(models.Model):
    idpropose = models.IntegerField(db_column='IDPROPOSE', primary_key=True)
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')
    idmembre = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='IDMEMBRE')

    class Meta:
        managed = False
        db_table = 'PROPOSE'
        unique_together = (('idmembre', 'idcocktail'),)


class Stocker(models.Model):
    idstocker = models.IntegerField(db_column='IDSTOCKER', primary_key=True)
    idingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IDINGREDIENT')
    idmembre = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='IDMEMBRE')
    enreserve = models.BooleanField(db_column='ENRESERVE', default=0)

    class Meta:
        managed = False
        db_table = 'STOCKER'
        unique_together = (('idmembre', 'idingredient'),)
