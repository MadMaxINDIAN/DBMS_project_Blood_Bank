from django.db.models.signals import post_save
from django.db import models
from blood_bank_app.models import *

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
class Donor(models.Model):
    name= models.CharField(max_length=30)
    dob = models.DateField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=128, choices=b_group_choices)
    quantity = models.IntegerField()
    disease_infection = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

def add_donor_trigger (sender, instance, created, **kwargs):
    if created:
        blood_stock = Blood_Stock.objects.get(blood_group=instance.blood_group)
        blood_stock.quantity = blood_stock.quantity + instance.quantity
        blood_stock.save()

post_save.connect(add_donor_trigger, sender=Donor)