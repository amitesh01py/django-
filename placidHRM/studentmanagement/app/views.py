from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import Courses, Students, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    return render(request, 'app/signup.html')

def index(request):
    return render(request, 'app/index.html') 


def signupform(request):
    if request.method == 'POST':
        name=request.POST['name']
        e_mail=request.POST['email']
        password=request.POST['password']
        if name == "":
            messages.error(request, 'enter your name')
            return redirect('signup')
        elif e_mail == "":
            messages.error(request, 'enter your email')
            return redirect('signup')
        elif password == "":
            messages.error(request, 'enter password')
            return redirect('signup')
        elif User.objects.filter(e_mail=e_mail).exists():
            messages.error(request, 'email already exist')
            return redirect('/')
        else:
            User.objects.create(name=name, e_mail=e_mail, password=make_password(password) )
            return redirect('login')


def profile(request):
    return render(request,'app/profile.html')


def dashboard(request):
    courses= Courses.objects.all()
    student= Students.objects.all()
    student_count = Students.objects.all().count()
    course_count = Courses.objects.all().count()
    return render(request, 'app/dashboard.html',{'courses':courses, 'student':student, 'student_count':student_count, 'course_count':course_count})

def tables(request):
    return render(request, 'app/tables.html')

def viewstudents(request):
    courses= Courses.objects.all()
    student= Students.objects.all()
    return render(request,'app/viewstudents.html', {'courses':courses, 'student':student})


def addStudent(request):
    if request.method == 'POST':
        name=request.POST['Name']
        # fees=request.POST['Fees']
        college=request.POST['College']
        degree=request.POST['Degree']
        mobile=request.POST['Mobile']
        email=request.POST['Email']
        # duration=request.POST['Duration']
        description=request.POST['Description']
        Course_id=request.POST['Course']
        course = Courses.objects.get(id=Course_id)
        # s_fees=request.POST['Fees']
        # s_duration=request.POST['Duration']
        # if Students.objects.filter(e_mail=email).exists():
        #     messages.error(request, 'email already exist')
        #     return redirect('viewstudents')
        # else:
        Students.objects.create(name=name, college=college, degree=degree, mobile_num=mobile, e_mail=email, s_description=description, s_course=course)
        messages.success(request, 'student added successfully')
        student= Students.objects.all()
        return render(request, 'app/viewstudents.html', {'courses':Courses.objects.all(), 'student':student})            
            # return redirect('viewstudents')
    else:
        return render(request, 'app/viewstudents.html', {'courses':Courses.objects.all()})        


def notifications(request):
    return render(request, 'app/notifications.html')


def loginform(request):
    if request.method == 'POST':
        e_mail = request.POST['Email']
        User_password = request.POST['Password']
        if e_mail == "":
            messages.error(request, 'enter your email')
            return redirect('login')
        elif User.objects.filter(e_mail=e_mail).exists():
            obj=User.objects.get(e_mail=e_mail)
            password=obj.password 
            if check_password(User_password, password):
                messages.success(request, 'login successful')
                return redirect('/dashboard/')
            else:
                messages.error(request, 'password is incorrect')
                return redirect('login')
        else:
            messages.error(request, 'email or password are invalid')
            return redirect('login')
    else:
        return redirect('login')

def courses(request):
    crs=Courses.objects.all()
    return render(request, 'app/courses.html', {'Cors':crs})            

def addcourses(request):
    if request.method == 'POST':
        new_course=request.POST['Course']
        n_fee=request.POST['Fee']
        n_duration=request.POST['Duration']
        n_description=request.POST['Description']
        if Courses.objects.filter(course=new_course).exists():
            messages.error(request, 'course already exist')
            return redirect('courses')
        else:
            Courses.objects.create(course=new_course, fee=n_fee, duration=n_duration, description=n_description)
            messages.success(request, 'course added successfully')
            return redirect('courses')

def edit_course(request, id):
    course = Courses.objects.get(id=id)
    return render(request, 'app/edit_course.html', {'course':course})    

def update_course(request):
    return render(request, 'app/edit_course.html')            

# def employees(request):
    # return render(request, 'app/employees.html')

# def hostel_details(request):
    # return render(request, 'app/hostel_details.html')

def pg_dashboard(request):
    return render(request, 'app/pg_dashboard.html')

# def tenants(request):
    # return render(request, 'app/tenants.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


    