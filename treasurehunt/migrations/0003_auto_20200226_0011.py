# Generated by Django 3.0.3 on 2020-02-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasurehunt', '0002_auto_20200225_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='routeID',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]