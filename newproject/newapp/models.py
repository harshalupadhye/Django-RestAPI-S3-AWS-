from django.db import models
import uuid

# Create your models here.
class boot(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Email

class DisplayPhoto(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Created_at=models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    image = models.FileField()
    def __str__(self):
        return self.title
      
