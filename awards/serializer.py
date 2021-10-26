from rest_framework import serializers
from .models import *
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_title', 'project_image', 'project_description', 'pub_date', 'author', 'author_profile', 'link','country')
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'project_title', 'project_image', 'project_description', 'pub_date', 'author', 'author_profile', 'link','country')