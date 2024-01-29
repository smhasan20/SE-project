
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('loginst/',views.loginst,name ='loginst'),
    path('login_view/',views.login_view,name ='login_view'),
    path('login_student/',views.login_student,name ='login_student'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/',views.signup,name ='signup'),
    path('input_student_course/', views.input_student_course, name='input_student_course'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_course/', views.add_course, name='add_course'),
    path('login_teacherview/',views.login_teacherview, name='login_teacherview'),
    path('login_teacher/',views.login_teacher, name='login_teacher'),
    path('teacherActivity/',views.teacherActivity, name='teacherActivity'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('signupstudent/',views.signupstudent, name='signupstudent'),
    path('signupteacher/',views.signupteacher, name='signupteacher')


]