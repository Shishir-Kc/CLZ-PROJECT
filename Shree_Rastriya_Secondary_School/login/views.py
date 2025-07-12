from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.models import Student_info
from teacher.models import Teacher

def user_login(request):
    if request.method == "POST":
        user_code = request.POST.get('user_code')
        user_pass = request.POST.get('user_pass')

        try:
             try:
              student = Student_info.objects.get(student_code=user_code)
              user_name = student.user.username
             except Student_info.DoesNotExist:
               try: 
                 teacher = Teacher.objects.get(teacher_code = user_code)
                 user_name = teacher.user.username
               except Teacher.DoesNotExist:
                  messages.error(request,"user with that credentials does not exist ")
                  return redirect('login:login')
         
        except Student_info.DoesNotExist or Teacher.DoesNotExist:
            messages.error(request, "Failed to Login: Check your credentials!")
            return render(request, 'login/login.html')

       
        user = authenticate(username=user_name, password=user_pass)
        
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in scessfully ')
            return redirect("home:home")
        else:
            messages.error(request,'entered credentials are incorrect ! ')
            return redirect('login:login')
    
    return render(request, 'login/login.html')

@login_required
def user_logout(request):
   logout(request)
   return redirect("login:login")


def error_404(request,exception):
   return render(request,'error_404/404.html',status=404)


    
    