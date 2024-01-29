# myapp/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import Student,Teacher

class StudentBackend(ModelBackend):
    def authenticate(self, request, sId=None, password=None, **kwargs):
        try:
            student = Student.objects.get(sId=sId)
        except Student.DoesNotExist:
            return None

        if student.password == password:
            return student

        return None
class TeacherBackend(ModelBackend):
    def authenticate(self, request, tId=None, email=None, **kwargs):
        try:
            teacher = Teacher.objects.get(tId=tId, email=email)
        except Teacher.DoesNotExist:
            return None

        

        return teacher
