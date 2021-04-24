from django.db import models
from hospital.models import *
from blood_bank_app.models import *
from django.db.models.signals import post_save

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
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=128, choices=b_group_choices)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)

def add_order_trigger (sender, instance, created, **kwargs):
    if created:
        blood_stock = Blood_Stock.objects.get(blood_group=instance.blood_group)
        blood_stock.quantity = blood_stock.quantity - instance.quantity
        if blood_stock.quantity < 0:
            instance.delete()
        else:
            blood_stock.save()

post_save.connect(add_order_trigger, sender=Order)