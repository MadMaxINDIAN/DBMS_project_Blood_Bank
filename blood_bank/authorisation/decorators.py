from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticted_user_only(view_func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect("/")
        return view_func(req, *args, **kwargs)
    return wrapper_func

def authenticted_user_only(view_func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return view_func(req, *args, **kwargs)
        return redirect("/")
    return wrapper_func
