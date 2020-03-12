from .models import Comment
from django import forms

"""
form class that generates a model form for comments
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']