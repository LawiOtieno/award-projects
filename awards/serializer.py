from rest_framework import serializers
from .models import Profile,Awwards

class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'info')



class AwwardsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Awwards
        fields = ('user', 'title', 'description', 'links')
