from django.db import models


# Create your models here.

 
  
class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)