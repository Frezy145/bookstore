from django.db import models, transaction
# Models

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
    pages = models.IntegerField()
    summary = models.TextField(max_length = 500)
    image = models.ImageField(upload_to = 'bookimages') # we'll upload it on AWS s3 at the end
    access = models.CharField(max_length = 20, choices = ACCESS_CHOICES, default = AL,) # by default it will be ALL
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField (auto_now_add = True)
    
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
    
    

# Customer model to store Customers
class Customer(models.Model):
    
    # gender choices
    MAL = 'MALE'
    FEM = 'FEMALE'
    GENDER = [
        (MAL, 'Male'),
        (FEM, 'Female')
    ]
    
    firstname = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(max_length = 20, choices = GENDER)
    profile_image = models.ImageField(upload_to = 'profiles', null = True) # we'll add upload_to and default at the end
    created_at = models.DateTimeField(auto_now_add = True)
    
    # we'll come back to add methods if needed
    
    