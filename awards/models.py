from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    image = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=800)
    info = models.TextField(max_length=1500)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 




class Award_projects(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    links =models.URLField()

    def __str__(self):
        return self.title

    def save_award_projects(self):
        self.save()


    @classmethod
    def all_award_projects(cls):

        all_award_projects = cls.objects.all()
        return all_award_projects


    @classmethod
    def single_award_projects(cls,id):
        single_award_projects = cls.objects.filter(id=id)
        return single_award_projects

    @classmethod
    def user_award_projects(cls,user):
        user_award_projects = cls.objects.filter(user=user)
        return user_award_projects

    @classmethod
    def search_award_projects(cls,search_term):
        searched_award_projects = cls.objects.filter(title = search_term)
        return searched_award_projects 



class Rates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    award_projects_id = models.ForeignKey(Award_projects, on_delete=models.CASCADE)
    usability = models.IntegerField(default=1)
    design = models.IntegerField(default=1)
    content = models.IntegerField(default=1) 

    



class Comments(models.Model):
    award_projects_id = models.ForeignKey(Award_projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)

    def __str__(self):
        return self.user


    @classmethod
    def get_all_comments(cls,id):
        comments = cls.objects.filter(my_project_id = id)
        return comments

    def save_comments(self):
        self.save()

    def delete_comment(self):
        self.delete()
