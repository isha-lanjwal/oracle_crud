from django.shortcuts import render, redirect
from .models import Student, Course

def student_list(request):
    students = Student.objects.select_related('course').all()
    return render(request, 'student_list.html', {'students': students})

# Uses select_related('course') to perform a SQL join, pulling in the related Course data in one query (performance optimization).

# Without select_related, Django would run one query per student to fetch the related course.

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        Student.objects.create(name=name, age=age, course=course)
        return redirect('student_list')
    courses = Course.objects.all()
    return render(request, 'add_student.html', {'courses': courses})
