# Generated by Django 3.0.3 on 2020-02-12 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasurehunt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]