import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newproject.settings')
import django
django.setup()
from newapp.models import boot
import random
from faker import Faker

fakegen=Faker()
def populate(n=5):
    for entry in range(n):
        fake_name=fakegen.first_name()
        fake_email=fakegen.ascii_email()
        fake_pass=fakegen.password()
        boots = boot.objects.get_or_create(Name=fake_name,Email=fake_email,Password=fake_pass)[0]
if __name__=='__main__':
    print("populating script!")
    populate(6)
    print("population Completed!")
    
   
    
   