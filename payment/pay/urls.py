from django.conf.urls import url, include
from django.contrib import admin
from .views import reg

urlpatterns = [
    url(r'^reg/$', reg,name='register'),
    #url(r'^', include('pay.urls',namespace='pay')),
]
