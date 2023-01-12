from django.db import models

# Create your models here.

class Agent_Master(models.Model):

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    agent_id=models.CharField(unique=True,max_length=50)
    phone=models.CharField(default="", max_length=20)
    address=models.TextField(default="")
    is_status=models.BooleanField(default=True)
    
    added_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

class File_Data(models.Model):

    name=models.CharField(default="",max_length=100)
    phone=models.CharField(unique=True,max_length=50)
    agent_id=models.CharField(max_length=50)
    xl_data=models.JSONField(default={})
    campaign=models.CharField(default="",max_length=100)
    is_processed=models.BooleanField(default=False)
    # level_two=models.BooleanField(default=False)
    # campaign=models.CharField(default="",max_length=100)
    is_status=models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

