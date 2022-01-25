from django.db import models

# Create your models here.

class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    switches = models.TextField(max_length=250)