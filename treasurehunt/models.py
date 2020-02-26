from django.db import models
from django.utils import timezone


class Clue(models.Model):
    clueID = models.IntegerField(primary_key=True)
    clueText = models.CharField(max_length=255, default="NoClue")
    imageFilePath = models.CharField(max_length=255, default="NoPath")

    def __str__(self):
        return self.clueText


class Task(models.Model):
    taskID = models.IntegerField(primary_key=True)
    taskText = models.CharField(max_length=255, default="NoTask")
    taskAnswer = models.CharField(max_length=255, default="NoAnswer")

    def __str__(self):
        return self.taskText


class Location(models.Model):
    locationID = models.IntegerField(primary_key=True)
    clueID = models.ForeignKey(Clue, on_delete=models.PROTECT)
    taskID = models.ForeignKey(Task, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, default="NoName")
    address = models.CharField(max_length=255, default="NoAddress")
    description = models.CharField(max_length=255, default="NoDescription")

    def __str__(self):
        return self.name


class Team(models.Model):
    #teamID = models.IntegerField(primary_key=True)
    teamName = models.CharField(max_length=20)
    teamMembers = models.IntegerField(default=0)
    routeID = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName

    class Meta:
        ordering = ['-score']