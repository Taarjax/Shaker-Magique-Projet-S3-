# Generated by Django 3.1.3 on 2020-11-19 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cocktail',
            table='COCKTAIL',
        ),
        migrations.AlterModelTable(
            name='compte',
            table='COMPTE',
        ),
        migrations.AlterModelTable(
            name='contenir',
            table='CONTENIR',
        ),
        migrations.AlterModelTable(
            name='favori',
            table='FAVORI',
        ),
        migrations.AlterModelTable(
            name='ingredient',
            table='INGREDIENT',
        ),
        migrations.AlterModelTable(
            name='membre',
            table='MEMBRE',
        ),
        migrations.AlterModelTable(
            name='noter',
            table='NOTER',
        ),
        migrations.AlterModelTable(
            name='preference',
            table='PREFERENCE',
        ),
        migrations.AlterModelTable(
            name='propose',
            table='PROPOSE',
        ),
        migrations.AlterModelTable(
            name='stocker',
            table='STOCKER',
        ),
    ]