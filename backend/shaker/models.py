# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cocktail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    intitule = models.CharField(db_column='INTITULE', max_length=255)  # Field name made lowercase.
    illustrationurl = models.CharField(db_column='ILLUSTRATIONURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categorie = models.CharField(db_column='CATEGORIE', max_length=255)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    forcealc = models.IntegerField(db_column='FORCEALC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'COCKTAIL'


class Compte(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', unique=True, max_length=32)  # Field name made lowercase.
    passhash = models.CharField(db_column='PASSHASH', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=255)  # Field name made lowercase.
    datecreation = models.DateField(db_column='DATECREATION', blank=True, null=True)  # Field name made lowercase.
    derniereconnexion = models.DateField(db_column='DERNIERECONNEXION', blank=True, null=True)  # Field name made lowercase.
    enligne = models.IntegerField(db_column='ENLIGNE')  # Field name made lowercase.
    sessionid = models.CharField(db_column='SESSIONID', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    idmembre = models.ForeignKey('MEMBRE', models.DO_NOTHING, db_column='IDMEMBRE', blank=True, null=True)  # Field name made lowercase.

    class Meta: 
        managed = False;
        db_table = 'COMPTE'


class Contenir(models.Model):
    idcontenir = models.IntegerField(db_column='IDCONTENIR', primary_key=True)  # Field name made lowercase.
    idcocktail = models.ForeignKey('COCKTAIL', models.DO_NOTHING, db_column='IDCOCKTAIL')  # Field name made lowercase.
    idingredient = models.ForeignKey('INGREDIENT', models.DO_NOTHING, db_column='IDINGREDIENT')  # Field name made lowercase.
    quantite = models.IntegerField(db_column='QUANTITE')  # Field name made lowercase.
    unite = models.CharField(db_column='UNITE', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'CONTENIR'
        unique_together = (('idcocktail', 'idingredient'),)


class Favori(models.Model):
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')  # Field name made lowercase.
    idmembre = models.OneToOneField('MEMBRE', models.DO_NOTHING, db_column='IDMEMBRE', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'FAVORI'
        unique_together = (('idmembre', 'idcocktail'),)


class Ingredient(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    intitule = models.CharField(db_column='INTITULE', max_length=255)  # Field name made lowercase.
    degrealcool = models.IntegerField(db_column='DEGREALCOOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'INGREDIENT'


class Membre(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='PRENOM', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=32, blank=True, null=True)  # Field name made lowercase.
    daten = models.DateField(db_column='DATEN', blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='GENRE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idcompte = models.ForeignKey(Compte, models.DO_NOTHING, db_column='IDCOMPTE')  # Field name made lowercase.
    idhote = models.ForeignKey('self', models.DO_NOTHING, db_column='IDHOTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'MEMBRE'


class Noter(models.Model):
    idmembre = models.OneToOneField(Membre, models.DO_NOTHING, db_column='IDMEMBRE', primary_key=True)  # Field name made lowercase.
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')  # Field name made lowercase.
    note = models.IntegerField(db_column='NOTE')  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'NOTER'
        unique_together = (('idmembre', 'idcocktail'),)


class Preference(models.Model):
    idingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IDINGREDIENT')  # Field name made lowercase.
    idmembre = models.OneToOneField(Membre, models.DO_NOTHING, db_column='IDMEMBRE', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'PREFERENCE'
        unique_together = (('idmembre', 'idingredient'),)


class Propose(models.Model):
    idpropose = models.IntegerField(db_column='IDPROPOSE', primary_key=True)
    idcocktail = models.ForeignKey(Cocktail, models.DO_NOTHING, db_column='IDCOCKTAIL')  # Field name made lowercase.
    idmembre = models.ForeignKey(Membre, models.DO_NOTHING, db_column='IDMEMBRE')  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'PROPOSE'
        unique_together = (('idmembre', 'idcocktail'),)


class Stocker(models.Model):
    idstocker = models.IntegerField(db_column='IDSTOCKER', primary_key=True)
    idingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IDINGREDIENT')  # Field name made lowercase.
    idmembre = models.ForeignKey(Membre, models.DO_NOTHING, db_column='IDMEMBRE')  # Field name made lowercase.
    enreserve = models.BooleanField(db_column='ENRESERVE')  # Field name made lowercase.

    class Meta:
        managed = False;
        db_table = 'STOCKER'
        unique_together = (('idmembre', 'idingredient'),)

