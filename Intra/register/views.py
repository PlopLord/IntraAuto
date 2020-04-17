from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from main.models import Student , CustomUser

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
       
        if form.is_valid():
            form.save()
            if response.POST.get('role') == 'ST':
                a = get_object_or_404(CustomUser,email=response.POST.get('email'))
                b = Student(profile=a)
                b.save()
            
        
        return redirect("/")
    else:
        profile = response.user
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form, "profile":profile})


