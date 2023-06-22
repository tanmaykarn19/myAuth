from django.contrib import admin
from django.urls import path, include
from home import views 

urlpatterns = [
    path('', views.index, name = "home"), 
    path('loginuser', views.loginuser, name = "loginuser"), 
    path('logoutuser', views.logoutuser, name = "logoutuser"), 

]