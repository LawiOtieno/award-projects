from django import forms
from .models import Awwards, Profile, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectFormNew(forms.ModelForm):
    class Meta:
        model = Awwards
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'my_project_id']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
