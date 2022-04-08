from django.db import models

class CustomUser(models.Model):
    phone_number = models.CharField(max_length=100, unique = True)
    passowrd = models.CharField(max_length=500)
