# Generated by Django 3.0.3 on 2020-02-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasurehunt', '0004_auto_20200226_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='teamID',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamMembers',
            field=models.IntegerField(default=1),
        ),
    ]
