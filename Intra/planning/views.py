from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlanningForm
from main.models import Student , CustomUser
from .models import Planning

def add(response):
    if response.method == "POST":

        a = get_object_or_404(CustomUser,id=response.POST.get('instructor'))
        b = get_object_or_404(Student,profile_id=response.POST.get('student'))
        c = Planning(student=b,instructor=a,start=response.POST.get('start'),day=response.POST.get('day'),end=response.POST.get('end'),duration=response.POST.get('duration'),place=response.POST.get('place'))
        c.save()
            
        
        return redirect("/")
    else:
        profile = response.user
        form = PlanningForm()
    return render(response, "planning/add.html", {"form":form, "profile":profile})

def view(response):
    planning = Planning.objects.all()
    profile = response.user
    return render(response, "planning/view.html", {"planning":planning,"profile":profile})



