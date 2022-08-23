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
    user = request.user
    student = user.student_data.get()
    student_courses = student.courses_of_student.all()
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