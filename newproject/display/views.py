from django.shortcuts import render
import requests
import json

# Create your views here.
def login(request):
    return render(request, 'home.html')

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

    return render(request, 'temp.html', {'data':data})
