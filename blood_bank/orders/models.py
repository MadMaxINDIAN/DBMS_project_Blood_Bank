from django.db import models

# Create your models here.
class Order (models.Model):
    Hospital = models.CharField(max_length=100)
    A_plus = models.CharField(max_length=10)
    A_neg = models.CharField(max_length=10)
    B_plus = models.CharField(max_length=10)
    B_neg = models.CharField(max_length=10)
    AB_plus = models.CharField(max_length=10)
    AB_neg = models.CharField(max_length=10)
    O_plus = models.CharField(max_length=10)
    O_neg = models.CharField(max_length=10)

    

    def __str__(self):
        return self.name