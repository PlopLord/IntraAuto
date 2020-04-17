from django.db import models
from main.models import CustomUser, Student




class Planning(models.Model):
    student= models.ForeignKey(Student, related_name="students", on_delete=models.CASCADE)
    instructor= models.ForeignKey(CustomUser, related_name="instructors", on_delete=models.CASCADE)
    day = models.DateTimeField()
    start = models.TimeField()
    end = models.TimeField()
    duration = models.DurationField()
    place = models.CharField(max_length=250)
    # def __str__(self):
    #     return self.student.profile