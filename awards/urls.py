from django.conf.urls import  url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    
    path('profile/',views.profile,name ='profile'),
    path('comment/<int:id>/',views.comment,name='comment'),
    path('rate/<int:id>/',views.rates,name='rates'),
    path('new_project/',views.projects_new,name='new_project'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('api/profile/',views.ProfileList.as_view()),
    path('api/projects/',views.MyprojectsList.as_view()),

    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^single_project/(\d+)',views.singl_project,name='single_project'),
        
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    