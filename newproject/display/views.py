from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from newapp.models import boot
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.serializers import bootSerializer
from django.contrib.auth import authenticate
from django import forms

# Create your views here.
def login(request):
    return render(request, 'signup.html')
def signin(request):
    return render(request, 'signin.html')

def submitUser(request):
    Name = request.GET['name']
    Email = request.GET['Email']
    Password = request.GET['Password']
  

    url = "http://127.0.0.1:8000/boot/"

    payload = {"Name": Name, "Email":Email, "Password":Password}
    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data = response.text

    return render(request, 'temp.html')

def submitUserIn(request):
    Name = request.GET['name']
    Email = request.GET['Email']
    Password = request.GET['Password']

    url = "http://127.0.0.1:8000/submitin/"

    payload = {"Name": Name, "Email":Email, "Password":Password}
    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data = response.text

    print(data)
    #return
    def clean(self,*args,**kwargs):
        Name=self.cleaned_data.get('name')
        Password=self.cleaned_data.get('Password')
        print(Name)
        print(Password)

    print(Name,Password)
    if Name and Password:
        user = authenticate(Name=Name, Password=Password)
        print(user)
        if not user:
            raise forms.ValidationError('this user does not exists')
        elif not user.check_password(Password):
            raise forms.ValidationError('this user does exists but password is wrong')
        elif not user.is_active:
            raise forms.ValidationError('this user is already active')
        else:
            return render(request, 'temp.html')
            
    return super(submitUserIn,self).clean(*args,**kwargs)


    

    









    

   