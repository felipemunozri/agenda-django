from datetime import date
from django.db import models


# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    company = models.CharField(max_length=30, blank=True, null=True)
    creation_date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

