from django import forms
from django.core.exceptions import ValidationError

from treasurehunt.models import Team


class teamForm(forms.ModelForm):

    def clean_teamMembers(self):
        data = self.cleaned_data['teamMembers']
        if data < 1:
            raise ValidationError('Invalid Number of Players. Too Few')

        if data > 6:
            raise ValidationError('Invalid Number of Players. Too Many')

        return data

    class Meta:
        model = Team
        fields = ['teamName', 'teamMembers']
        labels = {'teamName': 'Team Name',
                  'teamMembers': 'Number of Players (1-6)'}