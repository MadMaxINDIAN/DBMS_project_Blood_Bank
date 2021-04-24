from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url="/u/login_user")
def home(req):
    context = {
        'A_plus': Blood_Stock.objects.get(blood_group='A+').quantity,
        'A_neg': Blood_Stock.objects.get(blood_group='A-').quantity,
        'B_plus': Blood_Stock.objects.get(blood_group='B+').quantity,
        'B_neg': Blood_Stock.objects.get(blood_group='B-').quantity,
        'AB_plus': Blood_Stock.objects.get(blood_group='AB+').quantity,
        'AB_neg': Blood_Stock.objects.get(blood_group='AB-').quantity,
        'O_plus': Blood_Stock.objects.get(blood_group='O+').quantity,
        'O_neg': Blood_Stock.objects.get(blood_group='O-').quantity,
        'authenticated' : req.user.is_authenticated
    }
    return render(req, 'home.html', context=context)
