from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    CHOICES = ( 
        ("IN", "Instructor"), 
        ("ST", "Student"), 
    )
    email = forms.EmailField(max_length = 254) 
    role = forms.MultipleChoiceField(choices = CHOICES) 
    class Meta:
        model = get_user_model()
        fields = ["email", "password1", "password2","role"]