from django.db import models, transaction
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#Book model in which we'll store books

class Book(models.Model):
    
    # preparing choices list that we will use in below
    AD = 'ADULTS'
    AL = 'ALL'
    ACCESS_CHOICES = [
        (AD,'Adults'),
        (AL,'All')
    ]
    
    name = models.CharField(max_length = 200, unique = True)
    autors = models.CharField(max_length = 200)
    number_of_pages = models.IntegerField()
    summary = models.TextField(max_length = 500)
    image = models.ImageField(upload_to = 'bookimages') # we'll upload it on AWS s3 at the end
    access = models.CharField(max_length = 20, choices = ACCESS_CHOICES, default = AL,) # by default it will be ALL
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField (auto_now_add = True)
    
    # return the name on admin site
    def __str__(self):
        return self.name
    
    # we'll use this method in serializers to disable books
    @transaction.atomic
    def disable(self):
        if self.active is False:
            return # return nothing
        self.active = False
        self.save()
    
    # we'll use this method in serializers to enable books
    @transaction.atomic
    def enable(self):
        if self.active is True:
            return # return nothing
        self.active = True
        self.save()
    
# User model to store Users 
class User(AbstractUser):
    """
    User is an override AbstractUser subclass.
    So it'll settle fields authentications questions. We don't need to authenticate again
    
    """
    
    # gender choices
    MAL = 'MALE'
    FEM = 'FEMALE'
    GENDER = [
        (MAL, 'Male'),
        (FEM, 'Female')
    ]
    
    age = models.IntegerField(default = 18) # need to put default to allow superuser creation with manage.py
    gender = models.CharField(max_length = 20, choices = GENDER)
    profile_image = models.ImageField(upload_to = 'profiles', null = True) # images stoked in bucket/profiles
    
    # return the name on admin site
    def __str__(self):
        return self.username

# generate token when we create a new user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


    
    