from django.contrib import admin
from django.urls import path
from display import views
from newapp.views import bootView



urlpatterns = [
  
    path('home/', views.login),
    path('submit/', views.submitUser, name="submit"),
    path('submitin/', views.submitUserIn, name="submitin"),
    
    path('home/signin',views.signin),
    path('home/signup',views.login),
    
]
 