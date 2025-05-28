from django.shortcuts import render,redirect
from .models import Teacher
# Create your views here.

def teacher_list(request):
    teachers=Teacher.objects.all()
    total=teachers.count()
    return render(request,'index.html',{'allteachers':teachers,'total':total})


def add_teachers(request):
    if request.method=="POST":
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        contact=request.POST.get('contact')
        email=request.POST.get('email')

        teacher=Teacher(
            name=name,
            subject=subject,
            contact=contact,
            email=email
        )
        teacher.save()
        return redirect('all-teachers')
    return render(request,"index.html")

def update_teacher(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        contact=request.POST.get('contact')
        email=request.POST.get('email')

        teacher=Teacher(
            id=id,
            name=name,
            subject=subject,
            contact=contact,
            email=email

        )
        teacher.save()
        return redirect('all-teachers')
    return render(request,'index.html',{'teacher':teacher}) 

def delete_teacher(request,id):
    teacher=Teacher.objects.filter(id=id)
    teacher.delete()
    return redirect('all-teachers')

