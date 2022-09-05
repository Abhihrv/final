from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here

#Index view for courses app
@login_required
def dashboard(request):
    student = request.user.student_data.get()
    currentSem = Current.objects.first().currentSemester
    currentStudentSem = StudentSemester.objects.filter(student=student, semester=currentSem).get()
    student_courses = student.courses_of_student.filter(semester = currentStudentSem)
    return render(request, "courses/dashboard.html", {
        "student_courses" : student_courses
    })

@login_required
def degree(request):
    student = request.user.student_data.get()
    mydegrees = student.degrees_of_student.all()
    return render(request, "courses/degree.html", {
        "mydegrees" : mydegrees
    })

@login_required
def getDegree(request, degree_id):
    mydegree = StudentDegree.objects.get(id=degree_id)
    return JsonResponse(mydegree.serialize(), safe=False)

@login_required
def getPreviousSem(request):
    student = request.user.student_data.get()
    current = Current.objects.first()
    previousSems = student.semester_student.filter(semester__start__lt=current.currentDateTime)
    return render(request, "courses/previous-semesters.html", {
        "previousSems" : previousSems
    })

@login_required
def course(request,course_code):
    course = Course.objects.get(code=course_code)
    student_course = StudentCourse.objects.get(student=Student.objects.get(user=request.user), course=course)
    return render(request, "courses/course.html", {
        "student_course" : student_course
    })