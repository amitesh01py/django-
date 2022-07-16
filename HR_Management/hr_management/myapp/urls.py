from django import views
from django.conf import settings
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
path('',views.index, name='login'),    
path('signup/', views.signup, name='signup'),
path('signupform/', views.signupform),
path('loginform/', views.loginform),
path('profile/', views.profile, name='profile'),
path('dashboard/', views.dashboard, name='dashboard'),
path('tables/', views.tables, name='tables'),
path('viewstudents/', views.viewstudents, name='viewstudents'),
path('notifications/', views.notifications, name='notifications'),

path('courses/', views.courses, name='courses'),
path('addcourses/', views.addcourses),

# path('employees/', views.employees, name='employees'),
# path('hostel_details/', views.hostel_details, name='hostel_details'),
path('pg_dashboard/', views.pg_dashboard, name='pg_dashboard'),
# path('tenants/', views.tenants, name='tenants'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
