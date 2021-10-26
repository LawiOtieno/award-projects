from rest_framework import serializers
from .models import Profile,Award_projects

class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'info')



class Award_projectsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Award_projects
        fields = ('user', 'title', 'description', 'links')        