from django.conf.urls import url
from django.urls import path
from django.urls.conf import include, include
from django.urls.resolvers import URLPattern
from rest_framework.authtoken import views
from.views import home


urlpatterns =[
    path('',home, name='api.home')
]
