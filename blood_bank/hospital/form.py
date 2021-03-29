from django.forms import ModelForm
from .models import *

class CreateHospital(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'