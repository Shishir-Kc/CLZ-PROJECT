from django.db import models

# below here are db for home ! 

class Header(models.Model):
    title = models.CharField(max_length=255,verbose_name="school _name")


    class Meta:
        verbose_name = "title name {schol name }"
        verbose_name_plural = "School name"

    def __str__(self):
     return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slides/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title or f"Slide {self.id}"

class News(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('Events', 'Events'),
        ('Student Life', 'Student Life'),
        ('Sports', 'Sports'),
        ('Announcements', 'Announcements'),
        ('Notice','Notice'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default='School News')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'News'
    
    def __str__(self):
        return f"{self.title} | Category = > {self.category} | " 

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    category = models.CharField(max_length=100, default='Academic Event')
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    CATEGORY = [ 
        ('Events','Events'),
        ('Activities','Activities'),
        ('Achievements','Achievements'),
        ('Sports','Sports'),
        ('Student Life', 'Student Life'),
        ('Academics', 'Academics'),
        ('Announcements', 'Announcements'),
    ]
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY,default="Activities")
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Gallery Image {self.title} |category = > {self.category} | "
    

class Quick_acess_academics(models.Model):
    academics = models.ImageField(upload_to='academics/')
    academics_description = models.CharField(max_length=255,default="N/a")
    
    class Meta:
        verbose_name_plural = "Quick_Acess_academics"

    def __str__(self):
        return f"Add image related to the context ! "
    
        
class Quick_acess_admission(models.Model):
    admission = models.ImageField(upload_to='admission/')
    admission_description = models.CharField(max_length=255,default="N/a")
     
    class Meta:
        verbose_name_plural = "Quick_Acess_admisison"

    def __str__(self):
        return f"Add image related to the context ! "
    

class Achievements (models.Model):
    student = models.IntegerField(verbose_name="No of Students ")
    teacher = models.IntegerField(verbose_name="No of Teachers")
    experience = models.IntegerField(verbose_name="experience")
    sucess_rate = models.IntegerField(verbose_name="Sucess_rate")
    Faculty = models.IntegerField(verbose_name="Number of Faculty`s",default=0)
    def __str__(self):
        return f" Numbers for achivements"
    
    class Meta:
        verbose_name_plural = "Achivement"


class Academics(models.Model):
    grade_low = models.ImageField(upload_to='grade/',null=True)
    low_des = models.TextField(verbose_name="Short description ",blank=False)
    grade_mid = models.ImageField(upload_to='grade/',null=True)
    mid_des = models.TextField(verbose_name="Short description ",blank=False)
    grade_high = models.ImageField(upload_to='grade/',null=True)
    high_des = models.TextField(verbose_name="Short description ",blank=False)

    class Meta:
        verbose_name = 'Academic Level'
        verbose_name_plural = 'Academic Levels'

    def __str__(self):
        return f"short info about classes ! "
    

class Head_faculty(models.Model):
    teacher_image = models.ImageField(upload_to='faculty/')
    teacher_name = models.CharField(max_length=100)
    teacher_social_link = models.TextField(verbose_name="social link Like [ facebook , Gmail ] only one !")
    teacher_faculty = models.CharField(max_length=50,verbose_name="teacher faculty name ")
    teacher_description = models.TextField(verbose_name="short info about the teacher")

    class Meta:
        managed = True
        verbose_name = 'Faculty_teacher_info'
        verbose_name_plural = 'Faculty_teacher_infos'

    def __str__(self):
        return f"{self.teacher_name} | {self.teacher_faculty} | "
    
class Academic_resources(models.Model):
  Course_Catalogs = models.FileField(upload_to='pdf/')
  Academic_Policies = models.FileField(upload_to='pdf/')
  Study_Guides = models.FileField(upload_to='pdf/')
  Academic_Calendar = models.FileField(upload_to='pdf/')

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Academic_resource'
    verbose_name_plural = 'Academic_resources'

  def __str__(self):
      return "here contains necessary resources for academic"
  

class Contact(models.Model):
    full_name = models.TextField(verbose_name="applicant_Name ")
    email = models.EmailField(verbose_name="applicant_Email")
    contact = models.IntegerField(verbose_name="applicant_contact")
    faculty = models.TextField(verbose_name="applicant_choosen_faculty")
    message = models.TextField(verbose_name="applicant_message")

    class Meta:
        verbose_name = "Applicant"

    def __str__(self):
        return f"admission inquerry from {self.full_name}"
    
