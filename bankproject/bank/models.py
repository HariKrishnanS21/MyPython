from django.db import models

# Create your models here.
class pdet(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.TextField(default="not given")
    mob=models.IntegerField()
    mail=models.EmailField()