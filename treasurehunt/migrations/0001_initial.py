# Generated by Django 3.0.3 on 2020-02-25 22:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('clueID', models.IntegerField(primary_key=True, serialize=False)),
                ('clueText', models.CharField(default='NoClue', max_length=255)),
                ('imageFilePath', models.CharField(default='NoPath', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('routeID', models.IntegerField(primary_key=True, serialize=False)),
                ('routeName', models.CharField(default='NoRoute', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.IntegerField(primary_key=True, serialize=False)),
                ('taskText', models.CharField(default='NoTask', max_length=255)),
                ('taskAnswer', models.CharField(default='NoAnswer', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamID', models.IntegerField(primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=20)),
                ('teamMembers', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=0)),
                ('routeID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='treasurehunt.Route')),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='NoName', max_length=20)),
                ('address', models.CharField(default='NoAddress', max_length=255)),
                ('description', models.CharField(default='NoDescription', max_length=255)),
                ('clueID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasurehunt.Clue')),
                ('taskID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treasurehunt.Task')),
            ],
        ),
    ]
