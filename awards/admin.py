from django.contrib import admin
from .models import Awwards,Rates,Profile,Comments

# Register your models here.
admin.site.register(Awwards)
admin.site.register(Profile)
admin.site.register(Rates)
admin.site.register(Comments)