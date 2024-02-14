from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    type = Course_Type.objects.all().order_by('course_type')[:8]
    return render(request, 'elearning/index.html', {'data': type})

@login_required
def dashboard_student(request):
    return render(request, 'elearning/dashboard-student.html')

@login_required
def dashboard_teacher(request):
    return render(request, 'elearning/dashboard-teacher.html')

def about(request):
    return render(request, 'elearning/about.html')

def contact(request):
    return render(request,'elearning/contact.html')

def courses(request):
    return render(request,'elearning/courses.html')

def register_student(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        

        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.role = User.STUDENT
            user.is_active = True
            user.save()
            
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request, 'elearning/register-student.html',
                  {'user_form': user_form,
                    
                    'registered': registered, })

def register_teacher(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        

        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.role = User.TEACHER
            user.is_active = True
            user.save()
            
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request, 'elearning/register-teacher.html',
                  {'user_form': user_form,
                    
                    'registered': registered, })

def student_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password )

        if user:
            if user.is_active and user.role == User.STUDENT:
                login(request, user)
                return HttpResponseRedirect('../dashboard')
            else:
                return HttpResponse("Your account is disabled or you are not registered as student")
            
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'elearning/student-login.html',)

def teacher_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password )

        if user:
            if user.is_active and user.role == User.TEACHER:
                login(request, user)
                return HttpResponseRedirect('../dashboard/<str:username')
            else:
                return HttpResponse("Your account is disabled or you are not registered as teacher")
            
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'elearning/teacher-login.html',)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')
