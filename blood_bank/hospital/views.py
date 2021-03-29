from django.shortcuts import render

# Create your views here.
def hospitals(req):
    return render(req, 'hospitals.html')