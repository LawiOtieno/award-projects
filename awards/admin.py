from django.contrib import admin
from .models import Award_projects,Rates,Profile,Comments

# Register your models here.

admin.site.register(Award_projects)
admin.site.register(Profile)
admin.site.register(Rates)
admin.site.register(Comments)
