from django.urls import path    
from . import views
urlpatterns = [
    path('',views.teacher_list,name='all-teachers'),
    # path('index.html/',views.teacher_list,name='all-teachers'),
    path('add-teacher',views.add_teachers,name='addteacher'),
    path('update-teacher/<str:id>',views.update_teacher,name='update'),
    path('delete-teacher/<str:id>',views.delete_teacher,name='delete'),

]
