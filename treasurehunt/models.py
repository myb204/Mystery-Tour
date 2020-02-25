from django.db import models
from django.utils import timezone

class Clue(models.Model):
    clueID = models.AutoField(primary_key=True)
    clueText = models.CharField(max_length=255)
    imageFilePath = models.CharField(max_length=255)

    def __str__(self):
        return self.clueText

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskText = models.CharField(max_length=255)
    taskAnswer = models.CharField(max_length=255)

    def __str__(self):
        return self.taskText

class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    clueID = models.ForeignKey(Clue, on_delete=models.PROTECT)
    taskID = models.ForeignKey(Task, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Route(models.Model):
    routeID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.routeID

class RouteLocationMapping(models.Model):
    routeID = models.ForeignKey(Route, on_delete=models.PROTECT)
    locationID = models.ForeignKey(Location, on_delete=models.PROTECT)

class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=20)

    def __str__(self):
        return self.teamName

class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    teamID = models.ForeignKey(Team, on_delete=models.PROTECT)
    routeID = models.ForeignKey(Route, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField()

    def __str__(self):
        return self.gameID