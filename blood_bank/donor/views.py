import uuid
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
def uniqueidgenerator():
    x = uuid.uuid4().int >> 64
    if x < 9223372036854775807:
        return x
    else:
        return uniqueidgenerator()

@login_required(login_url="/u/login_user")
def donor(req):
    form = CreateDonor()
    context = {
        'form': form,
        'authenticated' : req.user.is_authenticated
    }
    if req.method == 'POST':
        form = CreateDonor(req.POST)
        print(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/d/')
        else:
            print('Form Invalid')
    donor = Donor.objects.filter()
    context['donor'] = donor
    return render(req, 'donors.html', context= context)