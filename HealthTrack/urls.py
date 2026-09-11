from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('accounts.urls')
    ),

    path(
        'accounts/',
        include('accounts.urls')
    ),

    path(
        'appointments/',
        include('appointments.urls')
    ),

    path(
        'records/',
        include('records.urls')
    ),

    path(
        'analytics/',
        include('analytics.urls')
    ),

]
