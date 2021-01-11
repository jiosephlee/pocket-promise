from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200, unique = True)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default = "")

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgs = models.ManyToManyField(Organization)
    balance = models.FloatField(default = 0)

    def __str__(self):
        return self.user.username

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
