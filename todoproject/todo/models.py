from django.db import models

# Create your models here.
class todo(models.Model):
    task=models.TextField()
    prio=models.IntegerField()
    date=models.DateField()