from django.db import models
from django.utils import timezone


class Clue(models.Model):

    clueText = models.CharField(max_length=255, default="NoClue")
    imageFilePath = models.CharField(max_length=255, default="NoPath")

    def __int__(self):
        return self.id


class Task(models.Model):
    taskText = models.CharField(max_length=255, default="NoTask")

    def checkCorrect(self, guess):
        answer = Answer.objects.get(answerid=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def getAnswers(self):
        return Answer.objects.filter(taskID=self)

    def getAnswersList(self):
        return [(Answer.answerID, Answer.answerText) for answer in Answer.objects.filter(taskID=self)]

    def __str__(self):
        return self.taskText


class Answer(models.Model):
    answerID = models.AutoField(primary_key=True)
    taskID = models.ForeignKey(Task, on_delete=models.CASCADE)
    answerText = models.CharField(max_length=50)
    correct = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.answerText


class Location(models.Model):
    clueID = models.ForeignKey(Clue, on_delete=models.PROTECT)
    taskID = models.ForeignKey(Task, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, default="NoName")
    address = models.CharField(max_length=255, default="NoAddress")
    description = models.CharField(max_length=255, default="NoDescription")

    def __str__(self):
        return self.name


class Route(models.Model):
    routeID = models.AutoField(primary_key=True)
    routeName = models.CharField(max_length=255, unique=True)
    numOfLocations = models.IntegerField(default=1)

    def __str__(self):
        return self.routeName


    def getNextClue(self, currentClue):
        return [RouteLocationMapping.locationID.clueID for routelocationmapping in
                RouteLocationMapping.objects.filter(routeID=Team.routeID, orderInRoute=currentClue+1)]


class RouteLocationMapping(models.Model):
    routeID = models.ForeignKey(Route, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    orderInRoute = models.IntegerField(default=0)

    def __str__(self):
        return str(self.routeID) + " : " + str(self.locationID)

class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length=20)
    teamMembers = models.IntegerField(default=0)
    routeID = models.ForeignKey(Route, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName

    class Meta:
        ordering = ['-score']
