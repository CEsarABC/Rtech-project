from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo 

# Create your models here.

class project(models.Model):
    
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    repository = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=None)
    
    def __str__(self):
        return self.title
        
class servicesUpdate(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    project_id = models.ForeignKey(project, default=None)
    
    def __str__(self):
        return self.title