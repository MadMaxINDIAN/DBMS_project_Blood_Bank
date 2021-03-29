from django.forms import ModelForm
from .models import *

class CreateDonor(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'