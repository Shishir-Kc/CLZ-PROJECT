from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import models as mod
from django.contrib import messages
from django.core.mail import send_mail
from student.models import Student_info
from teacher.models import Teacher

def home(request):
    user_session ="guest"

    if request.user.is_authenticated:
     try:
         try:
          user_session= Student_info.objects.get(user=request.user)
        
         except:
           user_session= Teacher.objects.get(user=request.user)
           
     except:
         print("nope")

    name = mod.Header.objects.first()
    slider = mod.Slider.objects.all()
    news = mod.News.objects.all().order_by('-created_at')[:1]
    event = mod.News.objects.filter(category = 'Events').order_by('-created_at')[:1]
    photo = mod.GalleryImage.objects.all().order_by('-created_at')[:4]
    events = mod.Event.objects.all().order_by('-created_at')[:1]
    Quick_acess_academics = mod.Quick_acess_academics.objects.first()
    Quick_acess_admission = mod.Quick_acess_admission.objects.first()
    achivement = mod.Achievements.objects.first()

    context= {
        'title':name,
        'slides':slider,
        'news':news,
        'gallery_images':photo,
        'upcoming_events':events,
        'quick_acess_academics':Quick_acess_academics,
        'Quick_acess_admission':Quick_acess_admission,
        'achivement':achivement,
        'events':event,
        'user_session':user_session,
        

    } 
    return render(request,"home/index.html",context)

def academics(request):
    achivement = mod.Achievements.objects.first()
    grade = mod.Academics.objects.first()
    faculty = mod.Head_faculty.objects.all()
    resource = mod.Academic_resources.objects.first()
    context = { 
        'achivement':achivement,
        'grade':grade,
        'facultys':faculty,
        'resource':resource
}


    return render (request,"academics/academics.html",context)

def admission(request):
    return render (request,"admision/admision.html")

def news(request):
    news = mod.News.objects.all()
    context = { 
        'new_s':news,
    }
    return render(request,"News/news.html",context)


def gallery(request):
    images = mod.GalleryImage.objects.all()
    context = { 
        'images':images,

    }

    return render(request,'gallery/gallery.html',context)

def achivement(request):
    return render (request,'achivements/achivements.html')

def contact(request):
    if request.method == "POST":
        full_name = request.POST.get("name") 
        email = request.POST.get("email")
        contact = request.POST.get("phone")
        faculty = request.POST.get("subject")
        message = request.POST.get("message")
        subject = "to get admitted "

        data = mod.Contact(full_name=full_name,email=email,contact=contact,faculty=faculty,message=message)
        data.save()
        full_message = f"From: {full_name} <{email}>\n\nSubject: {subject}\n\n Full Name : {full_name} \n\n Contact :{contact} \n\n Email:{email}\n\n Faculty:{faculty} \n\nMessage:\n{message}"

        send_mail(
            subject=f"Contact Form: {subject}",
            message=full_message,
            from_email= email,
            recipient_list=[''],  #
            fail_silently=False,
        )



        messages.success(request,"Send Sucessfully ! ")
        return render(request,"contact/contact.html")
   



    return render(request,"contact/contact.html")


