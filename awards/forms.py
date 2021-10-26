from django import forms
from .models import Award_projects, Profile, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectFormNew(forms.ModelForm):
    class Meta:
        model = Award_projects
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'award_project_id']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']