from django.db import models

# Create your models here.

class Employee(models.Model):
    Desg =  models.CharField(max_length=100)
    Name = models.CharField(max_length=120)
    Image = models.ImageField(upload_to="emp_photo")

    def __str__(self):
        return self.Name
