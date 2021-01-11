from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orgs = models.ManyToManyField(Organization)

    def __str__(self):
        return self.user.username
