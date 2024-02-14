from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard_student, name='dashboard-student'),
    path('dashboard-teacher', views.dashboard_teacher, name='dashboard-teacher'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('register-student', views.register_student, name='register-student'),
    path('register-teacher', views.register_teacher, name='register-teacher'),
    path('student-login', views.student_login, name='student-login'),
    path('teacher-login', views.teacher_login, name='teacher-login'),
    path('logout/', views.user_logout, name='logout'),
]