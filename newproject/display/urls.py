from django.contrib import admin
from django.urls import path
from display import views



urlpatterns = [
  
    path('home/', views.login),
    path('submit/', views.submitUser, name="submit")
    
]
 