from django.shortcuts import render,redirect    
from .models import Student
# Create your views here.
def student_list(request):
    students=Student.objects.all()
    total=students.count()
    return render(request,'index1.html',{"allstudents":students,'total':total})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        contact = request.POST.get('contact')
        email = request.POST.get('email')

        student = Student(
            name=name,
            grade=grade,
            contact=contact,
            email=email
        )
        student.save()
        return redirect('all-students')
    return render(request, 'index1.html')


def update_student(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        student=Student(
            id=id,
            name=name,
            grade=grade,
            contact=contact,
            email=email 
        )
        student.save()
        return redirect('all-students')
    return render(request, 'index1.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('all-students')

