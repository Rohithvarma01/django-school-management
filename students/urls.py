from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list,name='all-students'),
    path('add-student', views.add_student, name='addstudent'),
    path('update-student/<str:id>', views.update_student, name='updatestudent'),
    path('delete-student/<str:id>', views.delete_student, name='deletestudent'),
    
]

