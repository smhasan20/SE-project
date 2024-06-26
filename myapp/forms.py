# myapp/forms.py
from django import forms
from .models import Course, Student, CourseAttendance, Teacher,ContinuousAssessment
from django.contrib.auth.hashers import make_password,check_password

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sId', 'sName', 'contactNo', 'Address', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return make_password(password)  

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = self.clean_password() 
        if commit:
            instance.save()
        return instance

class CourseAttendanceForm(forms.ModelForm):
    class Meta:
        model = CourseAttendance
        fields = ['student', 'course','attendance']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['tId', 'tName', 'contactNo', 'email','password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return make_password(password)  

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = self.clean_password() 
        if commit:
            instance.save()
        return instance

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cId', 'courseName', 'teacher']

class ContinuousAssessmentForm(forms.ModelForm):
    class Meta:
        model = ContinuousAssessment
        fields =['student','course','marks','comment']
