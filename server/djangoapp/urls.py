from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='register'),

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
