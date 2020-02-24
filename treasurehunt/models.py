from django.db import models
from django.utils import timezone

class Clue(models.Model):
    clueID = models.AutoField(primary_key=True)
    clueText = models.CharField(max_length=255)
    imageFilePath = models.CharField(max_length=255)

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskText = models.CharField(max_length=255)
    taskAnswer = models.CharField(max_length=255)

class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    clueID = models.ForeignKey(Clue, on_delete=models.CASCADE) ###Unsure###
    taskID = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

class Route(models.Model):
    routeID = models.AutoField(primary_key=True)
    location1 = models.ForeignKey(Location, on_delete=models.CASCADE)

class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=20)

class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
    routeID = models.ForeignKey(Route, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField()