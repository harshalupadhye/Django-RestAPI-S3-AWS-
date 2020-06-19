from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.models import boot
from newapp.serializers import bootSerializer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Create your views here.
class bootView(APIView):
    def get(self, request):
        queryset = boot.objects.filter(Email=request.data.get("Email")).values().first()
        return Response(queryset)

    def post(self, request):
        queryset = request.data
        serializer = bootSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
            emailSend(request.data.get("Email"),request.data.get("Name"))
        return Response({"success ": "the user with the name '{}' is update". format(save_data.name)})    
       
    
    def put(self, request, pk):
        queryset = get_object_or_404(boot.objects.all(), pk=pk)
        parsed_data=request.data
        serializer = bootSerializer(instance=queryset, data=parsed_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
        return Response({"success ": "the user with the name '{}' is update". format(save_data.name)})
        
    def delete(self, request, pk):
        queryset = get_object_or_404(boot.objects.all(), pk=pk)
        queryset.delete()
        return Response({"success ": "the user with the id '{}' is deleted". format(pk)})
    
def emailSend( email, Name):
        text_content= "Yay! you have successfully registered"
        subject="welcome to our page"
        template_name="emailactivation.html"
        context={
        
            "username":Name
        }
        from_Email = "paupadhye64@gmail.com"
        recipents = [email]
        html_content = render_to_string(template_name, context)
        
        email = EmailMultiAlternatives(subject, text_content,from_Email,recipents)
        email.attach_alternative(html_content,"text/html")
        email.send()
     
    

