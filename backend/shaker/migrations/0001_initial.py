# Generated by Django 3.1.1 on 2020-11-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('intitule', models.CharField(db_column='INTITULE', max_length=255)),
                ('illustrationurl', models.CharField(blank=True, db_column='ILLUSTRATIONURL', max_length=255, null=True)),
                ('categorie', models.CharField(db_column='CATEGORIE', max_length=255)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('forcealc', models.IntegerField(blank=True, db_column='FORCEALC', null=True)),
            ],
            options={
                'db_table': 'cocktail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('login', models.CharField(db_column='LOGIN', max_length=32, unique=True)),
                ('passhash', models.CharField(db_column='PASSHASH', max_length=255)),
                ('email', models.CharField(db_column='EMAIL', max_length=255, unique=True)),
                ('datecreation', models.DateField(blank=True, db_column='DATECREATION', null=True)),
                ('derniereconnexion', models.DateField(blank=True, db_column='DERNIERECONNEXION', null=True)),
                ('enligne', models.IntegerField(db_column='ENLIGNE')),
                ('sessionid', models.CharField(blank=True, db_column='SESSIONID', max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'compte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('intitule', models.CharField(db_column='INTITULE', max_length=255)),
                ('degrealcool', models.IntegerField(blank=True, db_column='DEGREALCOOL', null=True)),
            ],
            options={
                'db_table': 'ingredient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('prenom', models.CharField(blank=True, db_column='PRENOM', max_length=32, null=True)),
                ('nom', models.CharField(blank=True, db_column='NOM', max_length=32, null=True)),
                ('daten', models.DateField(blank=True, db_column='DATEN', null=True)),
                ('genre', models.CharField(blank=True, db_column='GENRE', max_length=1, null=True)),
            ],
            options={
                'db_table': 'membre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contenir',
            fields=[
                ('idcocktail', models.OneToOneField(db_column='IDCOCKTAIL', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.cocktail')),
                ('quantite', models.IntegerField(db_column='QUANTITE')),
                ('unite', models.CharField(blank=True, db_column='UNITE', max_length=16, null=True)),
            ],
            options={
                'db_table': 'contenir',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('idmembre', models.OneToOneField(db_column='IDMEMBRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.membre')),
            ],
            options={
                'db_table': 'favori',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noter',
            fields=[
                ('idmembre', models.OneToOneField(db_column='IDMEMBRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.membre')),
                ('note', models.IntegerField(db_column='NOTE')),
            ],
            options={
                'db_table': 'noter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('idmembre', models.OneToOneField(db_column='IDMEMBRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.membre')),
            ],
            options={
                'db_table': 'preference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Propose',
            fields=[
                ('idmembre', models.OneToOneField(db_column='IDMEMBRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.membre')),
            ],
            options={
                'db_table': 'propose',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stocker',
            fields=[
                ('idmembre', models.OneToOneField(db_column='IDMEMBRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shaker.membre')),
                ('enreserve', models.IntegerField(db_column='ENRESERVE')),
            ],
            options={
                'db_table': 'stocker',
                'managed': False,
            },
        ),
    ]