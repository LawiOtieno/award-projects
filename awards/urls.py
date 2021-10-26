from django.conf.urls import  url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    path('profile/',views.profile,name ='profile'),
    path('comment/<int:id>/',views.comment,name='comment'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    path('rate/<int:id>/',views.rates,name='rates'),
    path('newproject/',views.projects_new,name='newproject'),
    path('updatetprofile/',views.update_profile,name='updateprofile'),
    path('api/profile/',views.ProfileList.as_view()),
    path('api/projects/',views.MyprojectsList.as_view()),
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    