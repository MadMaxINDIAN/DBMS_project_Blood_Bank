from django.db import models

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
    
