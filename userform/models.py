from django.db import models
from datetime import date

# Create your models here.
class Userform(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100,blank=False)
    phone = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='User Form'
    
