from django import forms
from django.core.exceptions import ValidationError
from django.forms import *
from treasurehunt.models import Team, Route


class teamForm(ModelForm):
    def clean_teamMembers(self):
        data = self.cleaned_data['teamMembers']

        if data < 1:
            raise ValidationError('Invalid Number of Players. Too Few')

        if data > 6:
            raise ValidationError('Invalid Number of Players. Too Many')

        return data

    class Meta:
        model = Team
        fields = ['teamName', 'teamMembers', 'routeID']
        labels = {'teamName': 'Choose a Team Name',
                  'teamMembers': 'Number of Players (1-6)',
                  'routeID': 'Select a Route'}


class routeForm(ModelForm):
    def clean_numOfLocations(self):
        data = self.cleaned_data['numOfLocations']

        if data < 2:
            raise ValidationError('Invalid Number of Locations. Too Few')

        if data > 20:
            raise ValidationError('Invalid Number of Locations. Too Many')

        return data

    class Meta:
        model = Route
        fields = ['routeName', 'numOfLocations']
        labels = {'routeName': 'Name of your New Route',
                  'numOfLocations': 'Number of Locations (2-20)'}


class taskForm(forms.Form):
    def __init__(self, Task, *args, **kwargs):
        super(taskForm).__init__(*args, **kwargs)
        choices = [x for x in Task.getAnswersList()]
        self.fields["Answers"] = forms.ChoiceField(choices=choices, widget=RadioSelect)
