from django.forms import ModelForm
from .models import *

class CreateOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'