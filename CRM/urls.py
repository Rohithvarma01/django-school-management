
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.landing,name='home'),
    path('',include('teachers.urls')),
    path('students/', include('students.urls')),
]
