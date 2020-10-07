from django.db import models

# Create your models here.
class Boys(models.Model):
    name = models.CharField(max_length=200)
    tele = models.CharField(max_length=200)