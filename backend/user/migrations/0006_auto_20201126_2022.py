# Generated by Django 3.1.1 on 2020-11-26 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201126_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id_hote',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
