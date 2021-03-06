from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo

# Create your models here.
'''I have forgotten to add foreign keys to this data base
i need to organize a better model of data base to link my models
(this two models are separated and they are tables which can be linked )'''
'''update 29 november, new models for tables, one table for services,
one table to link service to project, adding foreing keys'''

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

class Services(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField(max_length=50)

    def __str__(self):
        return self.title

class ServicesUpdate(models.Model):

    project = models.ForeignKey(project, default=None)
    service = models.ForeignKey(Services, default=None)

    def __str__(self):
        return self.title
