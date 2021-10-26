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
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    