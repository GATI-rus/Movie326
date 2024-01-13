"""
URL configuration for Movie326 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views
from catalog.views import *
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('kino/all/', kinolist.as_view(), name='allkino'),
    # path('kino/<int:pk>/', kinodetail.as_view(), name='info'),
    path('kino/<int:pk>/', kinodetail, name='info'),
    path('director/all/', directorlist.as_view(), name='alldirector'),
    path('director/<int:pk>/', directordetail.as_view(), name='infodirector'),
    path('actor/all/', actorlist.as_view(), name='allactor'),
    path('actor/<int:pk>/', actordetail.as_view(), name='infoactor'),
    path('user/', include('django.contrib.auth.urls')),
    path('accounts/profile/', lambda request: index(request)),
    path('user/reg/', reg, name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('podpiska/<int:userid>/', topodpiska, name='podpiska'),
    path('search/', search_films, name='search'),

    # path('podpiska/plusbalance/', plusbalance, name='plusbalance'),
]
