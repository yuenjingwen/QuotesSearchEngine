from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import searchView, successView

urlpatterns = [
    path('search/', searchView, name='search'),
    path('success/', successView, name='success'),
    url(r'^', include('haystack.urls'))
]
