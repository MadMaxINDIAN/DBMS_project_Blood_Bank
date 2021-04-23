from django.shortcuts import render, redirect
from .form import *
from .models import *
from hospital.models import *

# Create your views here.
def orders(req):
    form = CreateOrder()
    print(form.as_p)
    if req.method == 'POST':
        form = CreateOrder(req.POST)
        if form.is_valid():
            print(type(form.cleaned_data['Hospital'][0]))
            order = Order(Hospital=form.cleaned_data['Hospital'][0],blood_group=form.cleaned_data['blood_group'],quantity=form.cleaned_data['quantity'] )
            print(order)
            return redirect('/o/')
        else:
            print('Form Invalid')
    orders = Order.objects.filter()
    
	# form = CreateOrder()
    # context =  'form': form
    # if req.method == 'POST':
    #     form = CreateOrder(req.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/o/')
    #     else:
    #         print('Form Invalid')
    # orders = Order.objects.filter()
    # context['orders'] = orders
    return render(req, 'orders.html', context={'form':form.as_p,'orders':orders})
