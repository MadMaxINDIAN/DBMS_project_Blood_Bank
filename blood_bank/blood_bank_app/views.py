from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/u/login_user")
def home(req):
    print(req.user)
    context = {
        'A_plus': 23,
        'A_neg': 17,
        'B_plus': 30,
        'B_neg': 45,
        'AB_plus': 8,
        'AB_neg': 15,
        'O_plus': 18,
        'O_neg': 32,
        'authenticated' : req.user.is_authenticated
    }
    return render(req, 'home.html', context=context)
