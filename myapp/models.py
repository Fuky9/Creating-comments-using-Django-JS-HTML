from django.db import models

# Create your models here.
class UserComments(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    comment = models.CharField(max_length = 1000)