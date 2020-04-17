from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from main.models import CustomUser, Student


class PlanningForm(forms.Form):
    STUDENT_CHOICES=[]
    for student in Student.objects.all():
        STUDENT_CHOICES.append((student.profile_id,student.profile))
    INSTRUCTOR_CHOICES=[]
    for user in CustomUser.objects.all():
        if user.role == "['IN']":
            INSTRUCTOR_CHOICES.append((user.id,user.email))

    student = forms.MultipleChoiceField(choices=STUDENT_CHOICES, label="Eleve")
    instructor = forms.MultipleChoiceField(choices=INSTRUCTOR_CHOICES, label="Moniteur")
    duration = forms.DurationField(label="Durée de la session en heure")
    place = forms.CharField(max_length=250, label="lieu")
