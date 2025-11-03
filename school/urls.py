from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_edit_course/', views.add_edit_course, name='add_edit_course'),
    path('courses/', views.course_list, name='course_list'),  # New URL pattern for course list
    path('add_edit_course/<int:course_id>/', views.add_edit_course, name='add_edit_course'),  # New URL pattern for editing a course
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),  # New URL pattern for deleting a course
]
