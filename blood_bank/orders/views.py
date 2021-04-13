from django.shortcuts import render, redirect
from .form import *

# Create your views here.
def orders(req):
	form = CreateHospital()
    context = {
        'form': form
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
    return render(req, 'orders.html', context=context)
