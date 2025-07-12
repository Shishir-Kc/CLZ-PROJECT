from django.db import models
from django.contrib.auth.models import User
from data_class.models import Class,Subject
from .code import generate_unique_code

class Parent_info(models.Model):
    parent_name = models.CharField(max_length=30,verbose_name="parent_name")
    contact = models.IntegerField()
    address = models.TextField()
    email = models.EmailField(verbose_name="parent`s Email")

    class Meta:
        verbose_name  = "Parent_info"

    def __str__(self):
     return f"{self.parent_name}"



class Student_info(models.Model):
    parent = models.ManyToManyField(Parent_info,verbose_name="Student`s parent")
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name = "Associated_Student",related_name="student")
    student_code = models.CharField(
        max_length=10,
        unique=True,
        default=generate_unique_code,
        editable=True,
        verbose_name="Student Code"
    )

    student_profile = models.ImageField(upload_to='student/',blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(verbose_name="student_age")
    # student_class = models.IntegerField(verbose_name="student_class")
    email = models.EmailField(verbose_name="student_email")
    student_class = models.ForeignKey(Class,on_delete=models.CASCADE,verbose_name="student_class")
    Roll_num = models.IntegerField(verbose_name="student_roll number",default=0)

    

    class Meta:
        verbose_name = "student_info" 

    def __str__(self):
        return self.first_name  + " " +self.last_name



