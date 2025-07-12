from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models as std_md
from Home import models as h_mod
from data_class import models as Data
from django.contrib.auth import logout
from teacher import models as teach
from django.contrib import messages
from django.core.mail import send_mail


@login_required
def student_dashboard(request):
   try: 
    news=h_mod.News.objects.filter(category="Notice").order_by('-created_at')[:3]
    student_content= std_md.Student_info.objects.get(user=request.user)
    data = Data.Assignments.objects.filter(classs = student_content.student_class).order_by('-uploaded_at')[:7]
    some_data = student_content.student_class.subjects.count()
    student_section = student_content.student_class.section
    roll_num = student_content.Roll_num
    context = {
        'new_s' :news,
        'student':student_content,
        'assignments':data,
        'total_subject': some_data,
        'student_section':student_section,
        'roll_num':roll_num,
    }
    return render(request,"dashboard/dashboard.html",context)
   except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')




@login_required
def test_100(request):
    return HttpResponse("hello")

@login_required
def student_setting(request):
   try:
    if request.method == "POST":
        current_password = request.POST.get('current_password')

        if request.user.check_password(current_password):
            new_password = request.POST.get('new_password')
            request.user.set_password(new_password)
            request.user.save()
         
        else:
            print("error") # need a 404 page 
    

    
    student_content= std_md.Student_info.objects.get(user=request.user)
    context = {
        'student': student_content,
    }
    return render(request,"setting/setting.html",context)

   except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')


@login_required
def teacher(request):
  try:
    student_content= std_md.Student_info.objects.get(user=request.user)
    teachers = teach.Teacher.objects.filter(teacher_class = student_content.student_class)
    context = {
        'student': student_content,
        'teachers':teachers,
    }
    return render(request,"teacher/teacher.html",context)

  except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')




# @login_required
# def student_books(request):
#     return render (request,"books/books.html")


@login_required
def student_project(request):
   try:
    if request.method == "POST":
        title = request.POST.get('title')
        subject_id= request.POST.get('subject')
        student_content= std_md.Student_info.objects.get(user=request.user)
        # print(student_content.student_class.id)
        file = request.FILES.get('file')
        description = request.POST.get('description')
        subject = Data.Subject.objects.get(id=subject_id)
        data = Data.Project(student=request.user.student,classs = student_content.student_class,title=title,pdf=file,description=description,subject=subject)
        data.save()
        student_data= std_md.Student_info.objects.get(user=request.user)
        full_name = student_data.first_name  + student_data.last_name
        teacher = teach.Teacher.objects.filter(
        teacher_class=student_data.student_class,
           subject=subject).distinct()
        
        full_message = f"{full_name} has uploaded the project named : {title} \n\n Subject : {subject} \n\n Check it now !"
        email = ""
        teacher_mail = []
        for i in teacher:
           print(i.email)
           print(i.first_name)
           teacher_mail.append(i.email)

        send_mail(
            subject=f"Project submission",
            message=full_message,
            from_email= email,
            recipient_list=teacher_mail,  #
            fail_silently=False,
        )

        messages.success(request,"uploaded Sucessfully ! ")
        return redirect ("student:project")

    student = std_md.Student_info.objects.get(user=request.user)
    project = Data.Project.objects.filter(student=student).order_by('-uploaded_at')

    context = { 
        'student':student,
        'projects':project,
        
    }
    return render (request,"project/project.html",context)

   except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')


@login_required
def student_news(request):
 try:
    student = std_md.Student_info.objects.get(user = request.user)
    news = h_mod.News.objects.all().order_by('-created_at')
    context ={
        'new_s':news,
        'student':student,

    }
    return render(request,"news/feed.html",context)
 except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')



@login_required
def student_assignment(request):
  try:
    student = std_md.Student_info.objects.get(user = request.user)
    data = Data.Assignments.objects.filter(classs = student.student_class).order_by('-uploaded_at')
    context = {
        'student':student,
        'assignments':data,
    }
    return render (request,'std_assignments/assignments.html',context)
  except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')




#  need to add delete function asap today ! 

@login_required
def std_project_delete(request):
  try: 
   studet = std_md.Student_info.objects.get(user=request.user)
   if request.method == "POST":
      id = request.POST.get('project_id')
      project = Data.Project.objects.get(id=id)
      project.delete()
      messages.success(request,"deleted sucessfully ! ")
      return redirect('student:project')
   else:
      messages.success(request,'unnable to do action ')
      return redirect('student:project')
  except:
     messages.error(request,'unnnable to acess this content ! ')
     return redirect('home:home')
  
@login_required
def std_logout(request):
 try:
    logout(request)
    return redirect('login:login')
 except:
       messages.error(request,'cant acess this conntent unless you are student ! ')
       return redirect('home:home')
