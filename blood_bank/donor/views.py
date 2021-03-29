import uuid
from django.shortcuts import render

# Create your views here.
def uniqueidgenerator():
    x = uuid.uuid4().int >> 64
    if x < 9223372036854775807:
        return x
    else:
        return uniqueidgenerator()

def donor(req):
    return render(req, 'donors.html')