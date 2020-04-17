from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser, Student
from django.urls import reverse
from django.db.models import F


def home(response):
    profile=(response.user)
    return render (response, "main/home.html",{"profile":profile})

def studentList(response):
    queryset = CustomUser.objects.filter(role=['ST'])
    profile = response.user
    return render (response, "main/studentList.html",{"students":queryset,"profile":profile})

def studentDetail(response,student_id):
    profile = response.user
    student = get_object_or_404(CustomUser, pk=student_id)
    return render(response, 'main/studentDetail.html', {'student': student,"profile":profile})

def studentDelete(response,student_id):
    CustomUser.objects.get(pk=student_id).delete()
    return HttpResponseRedirect(reverse("main:studentList"))

def addHours(response,student_id):
    if response.method == "POST":
        nbHours = response.POST.get('hour')
        student = get_object_or_404(Student,pk=student_id)
        student.remaining_hour = F('remaining_hour') + nbHours
        student.save()
        
        print(student)
        return redirect("/students/list")

def instructorList(response):
    queryset = CustomUser.objects.filter(role=['IN'])
    profile = response.user
    return render (response, "main/instructorList.html",{"instructors":queryset,"profile":profile})

def instructorDetail(response,instructor_id):
    profile = response.user
    instructor = get_object_or_404(CustomUser, pk=instructor_id)
    return render(response, 'main/instructorDetail.html', {'instructor': instructor,"profile":profile})

def instructorDelete(response,instructor_id):
    CustomUser.objects.get(pk=instructor_id).delete()
    return HttpResponseRedirect(reverse("main:instructorList"))