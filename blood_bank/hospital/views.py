from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import *

# Create your views here.
@login_required(login_url="/u/login_user")
def hospitals(req):
    form = CreateHospital()
    context = {
        'form': form,
        'authenticated' : req.user.is_authenticated
    }
    if req.method == 'POST':
        form = CreateHospital(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/h/')
        else:
            print('Form Invalid')
    hospital = Hospital.objects.filter()
    context['hospital'] = hospital
    return render(req, 'hospitals.html', context=context)
