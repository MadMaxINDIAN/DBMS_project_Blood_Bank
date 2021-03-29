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
    id = models.BigIntegerField(primary_key=True, unique=True)
    name= models.CharField(max_length=30)
    dob = models.DateField()
    address = models.TextField()
    contact = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=128, choices=b_group_choices)
    disease_infection = models.TextField()
    
    def __str__(self):
        return self.name
    
