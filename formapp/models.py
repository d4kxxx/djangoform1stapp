from django.db import models

# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length=30, null = True)
    phone = models.CharField(max_length=30, null = True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null= True)
    
    
        
    
    
    
    