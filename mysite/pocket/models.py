from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
