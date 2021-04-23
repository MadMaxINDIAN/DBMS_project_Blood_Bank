from django.db import models
from hospital.models import *

b_group_choices = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

# Create your models here.
class Order (models.Model):
    Hospital = models.ManyToManyField(Hospital ,null=False,blank=False)
    blood_group = models.CharField(max_length=128, choices=b_group_choices)
    quantity = models.IntegerField()

    

    def __str__(self):
        return self.Hospital.name