
from django.shortcuts import redirect, render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.views.decorators.csrf import csrf_protect
from myapp.models import Student,StudentCourse
from myapp.models import StudentCourse
from .forms import CourseForm, StudentCourseForm, StudentForm, TeacherForm

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .backends import StudentBackend, TeacherBackend



def login_view(request):
    if request.method == 'POST':
        # Check if 'sId' and 'password' keys exist in the request's POST data
        sId = request.POST.get('sId')
        password = request.POST.get('password')
        opi = sId
        print(opi)
        if sId is not None and password is not None:
            student = authenticate(request, sId=sId, password=password)
            
            if student is not None:
                auth_login(request, student)

                # Retrieve data for the data table
                data_table_data = StudentCourse.objects.filter(sId=student.sId).select_related('sId', 'cId').values(
                    'sId__sId', 'cId__cId', 'sId__sName', 'cId__courseName', 'ct1', 'ct2', 'ct3', 'attendance', 'comment'
                ).order_by('cId')

                # Generate graph data
                #ct1_data = [row['ct1'] for row in data_table_data]
                #ct2_data = [row['ct2'] for row in data_table_data]
                #ct3_data = [row['ct3'] for row in data_table_data]
                #course_names = [row['cId__courseName'] for row in data_table_data]

                # Creating a bar chart using Matplotlib
                #plt.figure(figsize=(6, 8))
                #plt.bar(course_names, ct1_data, label='CT1')
                #plt.bar(course_names, ct2_data, label='CT2')
                #plt.bar(course_names, ct3_data, label='CT3')
                #plt.xlabel('Course')
                #plt.ylabel('Marks')
                #plt.title('Performance Comparison')
                #plt.legend()
                #plt.ylim(0, 150)
                
                # Convert the plot to a base64 encoded image
                #buffer = BytesIO()
                #plt.savefig(buffer, format='png')
                #buffer.seek(0)
                #plot_data = base64.b64encode(buffer.read()).decode('utf-8')
                #plt.close()

                context = {
                    'data_table_data': data_table_data,
                    'student': student
                    #'plot_data': plot_data
                }

                return render(request, 'dashboard.html', context)
            else:
                return render(request, 'home.html')
        else:
            return render(request, 'login_student.html')

    return render(request, 'login_student.html')


def login_teacherview(request):
    if request.method == 'POST':
        tId = request.POST.get('tId')
        email = request.POST.get('email')
    
        teacher = authenticate(request, tId=tId, email=email)
       
        if teacher is not None:
            auth_login(request, teacher)
            
            return redirect('teacherActivity')  
        else:
            # Invalid login, show error message or handle as needed
            return render(request, 'login_teacher.html')

    
    return render(request, 'login_teacher.html')

def login_teacher(request):
    return render(request,'login_teacher.html')
def teacherActivity(request):
    return render(request,'teacherActivity.html')
def home(request):
    return render(request,'home.html')
def loginst(request):
    return render(request,'loginst.html')
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')
def login_student(request):
    return render(request,'login_student.html')



def dashboard(request):
    student = request.user  
    student_courses = StudentCourse.objects.filter(sId=student.sId)

    return render(request, 'dashboard.html', {'student': student, 'student_courses': student_courses})


def input_student_course(request):
    if request.method == 'POST':
        form = StudentCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_student_course')  # Redirect to a success page
    else:
        form = StudentCourseForm()

    return render(request, 'input_student_course.html', {'form': form})
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')  # Redirect to a student list page or another desired page
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_teacher')  # Redirect to a teacher list page or another desired page
    else:
        form = TeacherForm()

    return render(request, 'add_teacher.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')  # Rirect to a course list page or another desired page
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def signupteacher(request):
    return render(request,'signupStudent.html')
def signupstudent(request):
    return render(request,'signupTeacher.html')