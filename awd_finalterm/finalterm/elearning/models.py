from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin

# Create your models here.


class Course_Type(models.Model):
    course_type = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.course_type

class Courses(models.Model):
    course_type = models.ForeignKey(Course_Type, on_delete=models.DO_NOTHING)
    course_name = models.CharField(max_length=256, null=False, blank=False)
    course_outline = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.course_name


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)
    status = models.TextField(max_length=50, null=False, blank=False)
    STUDENT = 1
    TEACHER = 2
   
    ROLE_CHOICES = (
        (STUDENT, "Student"),
        (TEACHER, 'Teacher'),
        
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=False)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
        
class Registered_Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course_name = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.course_name







