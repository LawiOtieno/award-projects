from re import A
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models import Awwards, Profile, Comments, Rates
from django.contrib.auth.models import User
from .forms import CommentForm, UpdateProfileForm, ProjectFormNew
from django.contrib import messages
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProfileListSerializer,AwwardsListSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.

def home(request):
    all_my_projects = Awwards.all_my_projects()
    return render(request,'welcome.html',{'all_my_projects':all_my_projects})


@login_required(login_url='/accounts/login/')
def profile(request):

    all_my_projects = Awwards.objects.filter(user = request.user)
    return render(request, 'profile.html', {'all_my_projects':all_my_projects})


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


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'projects' in request.GET and request.GET['projects']:
        search_term = request.GET.get('projects')
        searched_projects = Awwards.search_projects(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'my_projects':searched_projects}) 

    else:
        message = 'you have not entered anything to search'
        return render(request, 'search.html',{'message':message})

@login_required(login_url='/accounts/login/')
def comment(request,id):
    id=id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            my_projects = Awwards.objects.get(id=id)
            comment.my_projects_id = my_projects
            comment.save()
            return redirect('home')

        else:
            my_projects_id = id
            messages.information(request, 'fill all the fields')
            return redirect ('comment',id = my_projects_id)

    else:
        id = id
        form = CommentForm()
        return render(request, 'comment.html',{'form':form, 'id':id})


@login_required(login_url='/accounts/login/')
def rates(request,id):
    if request.method == 'POST':
        rates = Rates.objects.filter(id = id)
        for rate in rates:
            if rate.user == request.user:
                messages.info(request,'you only rate once')
                return redirect('singleproject',id)


        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')

        if design and usability and content:
            project = Awwards.objects.get(id=id)
            rate = Rates(design = design, usability = usability, content = content, my_project_id = project, user = request.user)
            rate.save()
            return redirect('singleproject',id)


        else:
            messages.info(request, 'Input all fields')
            return redirect('singleproject',id)


    else:
        messages.info(request,'Input all fields')
        return redirect('singleproject',id)            

            


@login_required(login_url='/accounts/login/')
def logout_request(request):
    """
    The function logs out user
    """                       

    logout(request)
    return redirect('home')



@login_required(login_url='/accounts/login/')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

        else:
            form = UpdateProfileForm(request.POST,request.FILES)
            return render(request,'update_profile.html',{'form':form})



@login_required(login_url='/accounts/login/')
def single_project(request,id):
    projects = Awwards.objects.get(id=id)
    comments = Comments.objects.filter(my_projects_id =id)
    rates = Rates.objects.filter(my_projects_id =id)
    designrate = []
    usabilityrate = []
    contentrate = []
    if rates:
        for rate in rates:
            designrate.append(rate.design)
            usabilityrate.append(rate.usability)
            contentrate.append(rate.content)

        total = len(designrate)*10
        design =round(sum(designrate)/total*100,1)
        usability =round(sum(usabilityrate)/total*100,1)
        content = round(sum(contentrate)/total*100,1)
        return render(request,'singleproject.html',{'projects':projects, 'comments':comments, 'design':design, 'usability':usability, 'content':content}) 

    else:
        design = 0
        usability = 0
        content = 0

        return render(request,'singleproject.html', {'projects':projects,'comments':comments,'design':design, 'usability':usability,'content':content}) 


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        plist = Profile.objects.all()
        serializers = ProfileListSerializer(plist,many=True)
        return Response(serializers.data) 

    def post(self, request, format=None):
        serializers = AwwardsListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)     


class MyprojectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        prolist = Awwards.objects.all()
        serializers = AwwardsListSerializer(prolist,many=True)
        return Response(serializers.data) 

    def post(self, request, format=None):
        serializers = AwwardsListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)             

