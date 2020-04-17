from django.urls import path
from . import views

app_name = "planning"
urlpatterns = [
path("add/", views.add, name="add"),
path("view/", views.view, name="view"),
]