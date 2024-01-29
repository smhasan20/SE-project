from contextlib import nullcontext
from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

class Student(models.Model):
    sId = models.IntegerField(primary_key=True)
    sName = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=15)
    Address = models.TextField()
    password = models.CharField(max_length=12, default=make_password('default_password'))
    last_login = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.sName


class Teacher(models.Model):
    tId = models.IntegerField(primary_key=True)
    tName = models.CharField(max_length=255)
    contactNo = models.CharField(max_length=15)
    email = models.EmailField()
    last_login = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.tName

class Course(models.Model):
    cId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseName

class StudentCourse(models.Model):
    sId = models.ForeignKey(Student, on_delete=models.CASCADE)
    cId = models.ForeignKey(Course, on_delete=models.CASCADE)
    ct1 = models.DecimalField(max_digits=5, decimal_places=2)
    ct2 = models.DecimalField(max_digits=5, decimal_places=2)
    ct3 = models.DecimalField(max_digits=5, decimal_places=2)
    attendance = models.CharField(default="0%",max_length=5)
    comment = models.TextField(default= " ")


    def __str__(self):
        student_name = self.sId.sName
        course_name = self.cId.courseName
        return f"{student_name} - {course_name}"
