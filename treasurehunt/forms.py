from django.forms import *
from treasurehunt.models import Team, Route, Task, Answer, RouteLocationMapping


class teamForm(ModelForm):
    def clean_teamMembers(self):
        data = self.cleaned_data['teamMembers']

        if data < 1:
            raise ValidationError('Invalid Number of Players. Too Few')

        if data > 10:
            raise ValidationError('Invalid Number of Players. Too Many')

        return data

    def getTeamMembers(self):
        data = self.cleaned_data['teamMembers']
        return data

    def getSelectedRoute(self):
        data = self.cleaned_data['routeID']
        return str(data)

    def getScore(self):
        data = self.cleaned_data['score']
        return str(data)

    class Meta:
        model = Team
        fields = ['teamName', 'teamMembers', 'routeID']
        labels = {'teamName': 'Choose a Team Name',
                  'teamMembers': 'Number of Players (1-10)',
                  'routeID': 'Select a Route'}


class routeForm(ModelForm):
    class Meta:
        model = Route
        fields = ['routeName']
        labels = {'routeName': 'Name of your New Route'}


class routeMappingForm(ModelForm):
    class Meta:
        model = RouteLocationMapping
        fields = ['locationID', 'orderInRoute']
        labels = {'locationID': 'Location',
                  'orderInRoute': 'Order'}


class taskForm(forms.Form):
    def __init__(self, task, *args, **kwargs):
        super(taskForm, self).__init__(*args, **kwargs)

        currentAnswers = [x for x in task.getAnswersList()]
        print(task)
        print(currentAnswers)

        self.fields['answers'] = ChoiceField(choices=currentAnswers, widget=RadioSelect)