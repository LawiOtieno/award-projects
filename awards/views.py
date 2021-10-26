from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models import Award_projects, Profile, Comments, Rates
from django.contrib.auth.models import User
from .forms import CommentForm, UpdateProfileForm, ProjectFormNew
from django.contrib import messages
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileListSerializer,Award_projectsListSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.

def home(request):

    all_projects = Award_projects.all_projects()


    return render(request,'welcome.html',{'all_projects':all_projects})


@login_required(login_url='/accounts/login/')
def profile(request):

    all_projects = Award_projects.objects.filter(user = request.user)
    return render(request, 'profile.html', {'all_projects':all_projects})


@login_required(login_url='/accounts/login/')
def projects_new(request):
    if request.method=='POST':
        form = ProjectFormNew(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit = False)
            projects.user = request.user
            projects.save()

            return redirect('home')

    else:
        form = ProjectFormNew()
    return render(request, 'new_project.html',{'form':form})



