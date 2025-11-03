from django.shortcuts import render, redirect
from .models import Student, Course

def add_edit_course(request, course_id=None):
    if course_id:
        course = Course.objects.get(id=course_id)
    else:
        course = None

    if request.method == 'POST':
        name = request.POST['name']
        instructor = request.POST['instructor']
        if course:
            course.name = name
            course.instructor = instructor
            course.save()
        else:
            Course.objects.create(name=name, instructor=instructor)
        return redirect('course_list')

    return render(request, 'add_edit_course.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course_list')

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

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')



