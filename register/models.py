from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254, unique = True)
    password = models.CharField(max_length=100)
    isPromoter = models.BooleanField(default=False)
