from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=70, unique=True)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    

   