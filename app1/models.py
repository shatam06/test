from django.db import models
from django.contrib.auth.models import User



genterch=(
    ('male','male'),
    ('female','female')
)


class data(models.Model):
    #user= models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.
    name=models.CharField(max_length=100)
    phone=models.PositiveIntegerField(unique=True)
    address=models.CharField(max_length=500)
    birthday=models.CharField(max_length=100)
    general=models.CharField(choices=genterch,max_length=9)
    password=models.CharField(max_length=50)




