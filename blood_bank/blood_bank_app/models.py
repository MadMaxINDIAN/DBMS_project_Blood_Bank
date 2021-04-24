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
class Blood_Stock(models.Model):
    blood_group = models.CharField(max_length=128, choices=b_group_choices)
    quantity = models.IntegerField()

    def __str__(self):
        return self.blood_group
    