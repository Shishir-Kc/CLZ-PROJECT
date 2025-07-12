from django.urls import path
from . import views


app_name = "teacher"
urlpatterns = [
    path('',views.teacher_dashboard,name="teacher_dashboard"),
    path('class/',views.teacher_class,name="teacher_class"),
    path('assignments/',views.student_assignments,name="assignments"),
    # path('exam/',views.exam,name="exam"),
    path('students/',views.students_list,name="student_list"),
    path('settings/',views.teacher_settings,name="settings"),    
    path('project/review/',views.student_project,name="project_submitted"),
    # path('schedule/',views.teacher_schedule,name="schedule"),
    path('upload/assignment/',views.upload_assignment,name="upload_assignment"),
    path('teacher/logout/',views.teacher_logout,name="logout"),
    path('upload/news/',views.upload_news,name="upload_news"),
    path('delete/news',views.delete_news,name="delete_news"),
    path('upload/Gallery/',views.upload_gallery,name='upload_gallery'),
    path('delete/image/',views.delete_gallery,name="delete_image"),
    
    
]



