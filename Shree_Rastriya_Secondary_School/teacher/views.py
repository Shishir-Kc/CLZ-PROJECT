from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models 
from student import models as std
# from data_class import project
from data_class.models import Project,Assignments,Class,Subject
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.core.mail import send_mail
from student import models as stu
from Home import models as H



@login_required
def teacher_dashboard(request):
    try:
       
     teacher = models.Teacher.objects.get(user=request.user)
     teacher_content = models.Teacher.objects.get(user=request.user)
     teacher_classes = teacher.teacher_class.all()
     total_students = std.Student_info.objects.filter(student_class__in=teacher_classes).count()
     assignment = teacher.assignments.count()
    # projects = Project.objects.filter(classs__in=teacher_classes)[:4]
     projects = Project.objects.filter(
     classs__in=teacher.teacher_class.all(),
     subject__in=teacher.subject.all()).order_by('-uploaded_at')[:4]
    # print(projects)

    # print(assignment)

     context = {
         'teacher':teacher_content,
         'std_num':total_students,
         'projects':projects,        
     }
    # print(teacher_content.teacher_class)
     return render(request,"teach_dashboard/dashboard.html",context)
    except:
       messages.error(request,"you have no acess to this site ! ")
       return redirect('home:home')
    
@login_required
def teacher_class(request):
    try:
     teacher = models.Teacher.objects.get(user=request.user)
     classes = teacher.teacher_class.all()
     context = {
         'teacher':teacher,
         'classes':classes
     }
     # print(teacher)


     return render(request,"teacher_class/class.html",context)

    except:
        messages.error(request,"you have no acess to this site ! ")
        return redirect('home:home')


@login_required
def student_assignments(request):
  try:  
    if request.method == "POST":
     id = request.POST.get('assignment_id')
     try:
        assignments = Assignments.objects.get(id=id)
        assignments.delete()
        # print("assignment deleted.")
     except Assignments.DoesNotExist:
        
        return redirect('teacher:assignments')

    teacher = models.Teacher.objects.get(user=request.user)
    assignments = Assignments.objects.filter(teacher=teacher).order_by('-uploaded_at')
    context = {
        'teacher':teacher,
        'assignments': assignments,
    }
    
    return render(request,"assignments/assignments.html",context)
  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')

@login_required
def upload_assignment(request):
  try:  
    if request.method == "POST":
     title = request.POST.get('title')
     file = request.FILES.get('note_file')
     subject_raw = request.POST.get('subject')
     Classs_raw= request.POST.get('class')
     content = request.POST.get('description')
    #  print(title,subject,content,Classs,section)
     subject = Subject.objects.get(id=subject_raw)
     classs = Class.objects.get(id=Classs_raw) 
    # print(subject,classs)
    data = Assignments(teacher=request.user.teacher,subject=subject,classs=classs,title=title,content=content,pdf_file=file)
    data.save()   
    teacher = models.Teacher.objects.get(user=request.user)
    email =teacher.email
    full_name = teacher.first_name  + teacher.last_name
    message = f"Students note of {subject} has been uploaded ! "
    students = stu.Student_info.objects.filter(student_class__in= teacher.teacher_class.all())
    student_email = []

    for i in students:
       student_email.append(i.email)
    full_message = f"From: {full_name} \n\nSubject: {subject}\n\n Full Name : {full_name} \n\n \n\n Note uploaded:\n {message}"
    send_mail(
            subject=f"Contact Form: {subject}",
            message=full_message,
            from_email= email,
            recipient_list=student_email,  #
            fail_silently=False,
        )


    messages.success(request, f' Uploaded successfully! Your students can now access this note.')
    return redirect('teacher:assignments')

  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')

# def exam(request):
#     return render(request,"exam/exam.html")

@login_required
def students_list(request):
  try:  
    teacher = models.Teacher.objects.get(user=request.user)
    student_data = std.Student_info.objects.filter(student_class__in= teacher.teacher_class.all())
    context = {
        'teacher':teacher,
        'students':student_data,
    }
    return render(request,"students/students.html",context)

  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')


@login_required
def teacher_settings(request):
  try:  
    if request.method == 'POST':
        current_password = request.POST.get('current_password')

        if request.user.check_password(current_password):
            new_password = request.POST.get('new_password')
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password updated successfully!")
            print("updated")
        else:
            messages.error(request, "Current password is incorrect.")

    teacher = models.Teacher.objects.get(user=request.user)

    
    context = {
        'teacher':teacher
    }
    return render(request,"settings/settings.html",context)
  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')

@login_required
def student_project(request):
  try:  
    if request.method == "POST":
        id = request.POST.get('project_id')
        action = request.POST.get('action_type')
        if action == "reject":
            status = "Rejected"
        else:
            status = "Approved"


        try:
            project_state = Project.objects.get(id=id)
            project_state.status = status
            project_state.save()
            if status == "Rejected":
             messages.error(request,f" {status} project ")
            else:
               messages.success(request,f" {status} project ")
        except Project.DoesNotExist:
           return HttpResponse('PROJECT NOT FOUND ! ')
        
    teacher = models.Teacher.objects.get(user=request.user)
    projects = Project.objects.filter(
    classs__in=teacher.teacher_class.all(),
    subject__in=teacher.subject.all()).order_by('-uploaded_at')
    approved_projects = Project.objects.filter(status="Approved",subject__in = teacher.subject.all()).count()
    rejected_projects =  Project.objects.filter(status="Rejected",subject__in = teacher.subject.all()).count()
    pending_projects =  Project.objects.filter(status="Pending",subject__in = teacher.subject.all()).count()
    context = {
        'projects':projects,
        'teacher':teacher,
        'approved':approved_projects,
        'rejected':rejected_projects,
        'pending': pending_projects,
    }
    return render(request,"student_project/project.html",context)

  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')


# @login_required
# def teacher_schedule(request):
#     teacher = models.Teacher.objects.get(user=request.user)
#     context = { 
#        'teacher':teacher,
#     }

#     return render(request,"schedule/schedule.html",context)



@login_required
def upload_news(request):
  try:
   if request.method == "POST":
      title = request.POST.get('title')
      category = request.POST.get('category')
      content = request.POST.get('content')
      file = request.FILES.get('image')
      
      data = H.News(title=title,description=content,image=file,category=category)
      data.save()
      messages.success(request,"Uploaded Sucessfully ! ")
      return redirect ("teacher:upload_news")

   teacher = models.Teacher.objects.get(user = request.user)
   news = H.News.objects.all()


   context = {
      'teacher':teacher,
       'new_s':news
   }
   return render(request,'news_upload/news.html',context)

  except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')


@login_required
def upload_gallery(request):
   try:

      if request.method == "POST":
         print('post method ')
         title = request.POST.get('title')
         category = request.POST.get('category')
         image = request.FILES.get('image_file')
         data = H.GalleryImage(title=title,image=image,category=category)
         data.save()
         messages.success(request,'Image uploaded Sucessfully ! ')
         return redirect('teacher:upload_gallery')
         

      gallery = H.GalleryImage.objects.all()
      teacher_data = models.Teacher.objects.get(user=request.user)
      context = { 
         'images':gallery,
         'teacher':teacher_data
      }

      return render(request,'gallery_upload/gallery.html',context)



   except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')
      


@login_required
def delete_gallery(request):
   try:
      if request.method == "POST":
         id = request.POST.get('image_id') 
         image_data = H.GalleryImage.objects.get(id = id)
         image_data.delete()
         messages.success(request,'Image Deleted Sucessfully ! ')
         return redirect('teacher:upload_gallery')
   except:
      messages.error(request,"something went wrong ! ")
      return redirect('teacher:upload_gallery')
  


@login_required
def delete_news(request):
 try:
   if request.method == "POST":
        try:
         news_id = request.POST.get('news_id')
         news = H.News.objects.get(id=news_id)
         news.delete()
         messages.success(request, "Deleted successfully!")
        except H.News.DoesNotExist:
         messages.error(request, "News not found.")
        except Exception as e:
         messages.error(request, f"Failed to delete: {str(e)}")
    
        return redirect("teacher:upload_news")
   else:
   
      return redirect('teacher:upload_news')
 except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')

  
@login_required
def teacher_logout(request):
 try:
   logout(request)
   return redirect("login:login")
 except:
      messages.error(request,"you have no acess to this site ! ")
      return redirect('home:home')
