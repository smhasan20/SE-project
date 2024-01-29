# myapp/forms.py
from django import forms
from .models import Course, Student, StudentCourse, Teacher

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['sId', 'cId', 'ct1', 'ct2', 'ct3','attendance','comment']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sId', 'sName', 'contactNo', 'Address', 'password']

    def clean_password(self):
    
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['tId', 'tName', 'contactNo', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['cId', 'courseName', 'teacher']
