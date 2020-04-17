from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
path("", views.home, name="home"),
path("students/list", views.studentList, name="studentList"),
path("students/detail/<int:student_id>/", views.studentDetail, name="studentDetail"),
path("students/delete/<int:student_id>/", views.studentDelete, name="studentDelete"),
path("students/add_hour/<int:student_id>/", views.addHours, name="addHours"),
path("instructor/list/", views.instructorList, name="instructorList"),
path("instructor/detail/<int:instructor_id>", views.instructorDetail, name="instructorDetail"),
path("instructor/delete/<int:instructor_id>", views.instructorDelete, name="instructorDelete"),

]