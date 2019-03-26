from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    #additionals
    portfolio_site = models.CharField(max_length=100)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

