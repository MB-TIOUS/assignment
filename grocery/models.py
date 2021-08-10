from django.db import models
from datetime import datetime

# Create your models here.
class list_element(models.Model):
    id = models.AutoField(primary_key=True)
    un = models.CharField(max_length=100)
    iname = models.CharField(max_length=100)
    iquantity = models.CharField(max_length=100)
    istatus = models.CharField(max_length=100)
    idate = models.DateField()