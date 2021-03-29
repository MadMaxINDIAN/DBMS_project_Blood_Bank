from django.shortcuts import render

# Create your views here.
def home(req):
    context = {
        'A_plus': 23,
        'A_neg': 17,
        'B_plus': 30,
        'B_neg': 45,
        'AB_plus': 8,
        'AB_neg': 15,
        'O_plus': 18,
        'O_neg': 32,
    }
    return render(req, 'home.html', context=context)
