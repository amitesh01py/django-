from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import Courses, User
from django.contrib import messages

# Create your views here.
def signup(request):
    return render(request, 'myapp/signup.html')

def index(request):
    return render(request, 'myapp/index.html')

def signupform(request):
    if request.method == 'POST':
        name=request.POST['name']
        e_mail=request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(e_mail=e_mail).exists():
            messages.error(request, 'email already exist')
            return redirect('/')
        else:
            User.objects.create(name=name, e_mail=e_mail, password=password )
            return redirect('login')

def profile(request):
    return render(request,'myapp/profile.html')

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def tables(request):
    return render(request, 'myapp/tables.html')

def viewstudents(request):
    return render(request,'myapp/viewstudents.html')

def notifications(request):
    return render(request, 'myapp/notifications.html')

def loginform(request):
    if request.method == 'POST':
        e_mail = request.POST['Email']
        User_password = request.POST['Password']
        if User.objects.filter(e_mail=e_mail).exists():
            obj=User.objects.get(e_mail=e_mail)
            password=obj.password 
            if check_password(User_password, password):
                return redirect('/dashboard/')
            else:
                return HttpResponse('incorrect password')
        else:
            return HttpResponse('email does not registered')

def courses(request):
    crs=Courses.objects.all()
    return render(request, 'myapp/courses.html', {'Cors':crs})            

def addcourses(request):
    if request.method == 'POST':
        new_course=request.POST['Course']
        n_fee=request.POST['Fee']
        n_description=request.POST['Description']
        if Courses.objects.filter(course=new_course).exists():
            messages.error(request, 'course already exist')
            return redirect('courses')
        else:
            Courses.objects.create(course=new_course, fee=n_fee, description=n_description)
            return redirect('courses')

# def employees(request):
    # return render(request, 'myapp/employees.html')

# def hostel_details(request):
    # return render(request, 'myapp/hostel_details.html')

def pg_dashboard(request):
    return render(request, 'myapp/pg_dashboard.html')

# def tenants(request):
    # return render(request, 'myapp/tenants.html')
    