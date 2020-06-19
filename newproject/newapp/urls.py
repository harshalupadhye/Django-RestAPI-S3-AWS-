from django.contrib import admin
from django.urls import path
from newapp import views



urlpatterns = [
  
    path('boot/', views.bootView.as_view()),
    path('boot/<int:pk>', views.bootView.as_view()),
]
