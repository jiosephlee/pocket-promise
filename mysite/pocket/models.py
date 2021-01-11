from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Organization(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.name

#here is the code to do database on the terminal
#python manage.py shell
#from pocket.models import User, Organization
#Organization.objects.all()
#Organization.objects.filter(id=1)
#Organization.objects.filter(category__startswith='xxx')
#https://docs.djangoproject.com/en/3.1/intro/tutorial02/
#q=Organization(name="",category="")
#q.save()
#q.name
