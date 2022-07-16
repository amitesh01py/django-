from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255)
    e_mail=models.CharField(max_length=255)
    password=models.CharField(max_length=100, blank=True, null=True)
   
    
class Courses(models.Model):
    course=models.CharField(max_length=255)
    fee=models.FloatField()
    description=models.TextField()
    duration=models.CharField(max_length=100)
    # upload_image=models.ImageField(upload_to="courseimg", null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

    
class Students(models.Model):
    name=models.CharField(max_length=255)
    fees=models.FloatField()
    s_course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    college=models.CharField(max_length=255)
    degree=models.CharField(max_length=100)
    mobile_num=models.IntegerField()
    e_mail=models.CharField(max_length=100)
    duration=models.IntegerField()
    s_description=models.TextField()
    # upload_img=models.ImageField(upload_to="studentimg", null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

