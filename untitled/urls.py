from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from petition import views as petition_views

urlpatterns = [
    url(r'^$', petition_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^index/$', petition_views.index, name='index'),
    url(r'^index/$', petition_views.index, name='index'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^done/', petition_views.done, name='done'),
    #url(r'stop/', petition_views.stop, name='stop'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
