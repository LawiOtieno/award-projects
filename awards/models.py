from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    image = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=1200)
    info = models.TextField(max_length=1500)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 




class Awwards(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=1500)
    links =models.URLField()

    def __str__(self):
        return self.title

    def save_my_projects(self):
        self.save()


    @classmethod
    def all_my_projects(cls):

        all_my_projects = cls.objects.all()
        return all_my_projects


    @classmethod
    def single_my_projects(cls,id):
        single_my_projects = cls.objects.filter(id=id)
        return single_my_projects

    @classmethod
    def user_my_projects(cls,user):
        user_my_projects = cls.objects.filter(user=user)
        return user_my_projects

    @classmethod
    def search_my_projects(cls,search_term):
        searched_my_projects = cls.objects.filter(title = search_term)
        return searched_my_projects 



class Rates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    my_projects_id = models.ForeignKey(Awwards, on_delete=models.CASCADE)
    usability = models.IntegerField(default=1)
    design = models.IntegerField(default=1)
    content = models.IntegerField(default=1) 

    



class Comments(models.Model):
    my_projects_id = models.ForeignKey(Awwards, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=1200)

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
