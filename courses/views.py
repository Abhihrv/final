from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# User Tests
def student_check(user):
    return user.user_type.code == "ST"

#Index view for courses app
@login_required
@user_passes_test(student_check, redirect_field_name=None)
def dashboard(request):
    student = request.user.student_data.get()
    currentSem = Current.objects.first().currentSemester

    try:
        currentStudentSem = StudentSemester.objects.filter(student=student, semester=currentSem).get()
        student_courses = student.courses_of_student.filter(semester = currentStudentSem)
        return render(request, "courses/dashboard.html", {
            "student_courses" : student_courses
        })
    except ObjectDoesNotExist:
        return render(request, "courses/dashboard.html", {
            "student_courses" : [],
            "error": True,
            "errorMessage": "Please enroll in a semester and a course first" 
        })
        
    

@login_required
@user_passes_test(student_check, redirect_field_name=None)
def degree(request):
    student = request.user.student_data.get()
    mydegrees = student.degrees_of_student.all()
    if len(mydegrees) == 0:
        return render(request, "courses/degree.html", {
            "mydegrees" : mydegrees,
            "error": True,
            "errorMessage": "No Degree Found" 
        })
    return render(request, "courses/degree.html", {
        "mydegrees" : mydegrees
    })

@login_required
@user_passes_test(student_check, redirect_field_name=None)
def registerDegree(request):
    if request.method == "POST":
        student = request.user.student_data.get()
        degreeForm = DegreeForm(request.POST)
        if degreeForm.is_valid():
            degree = degreeForm.cleaned_data["degree"]
            studentdegree = StudentDegree(student=student, degree=degree)
            studentdegree.save()
            return HttpResponseRedirect(reverse("mydegree"))
    return render(request, "courses/registration.html", {
            "name": "Degree",
            "formUrl": "registerDegree",
            "registrationForm": DegreeForm()
        })

@login_required
def getDegree(request, degree_id):
    mydegree = StudentDegree.objects.get(id=degree_id)
    return JsonResponse(mydegree.serialize(), safe=False)


@login_required
@user_passes_test(student_check, redirect_field_name=None)
def course(request,course_code):
    course = Course.objects.get(code=course_code)
    student_course = StudentCourse.objects.get(student=Student.objects.get(user=request.user), course=course)
    return render(request, "courses/course.html", {
        "student_course" : student_course
    })

@login_required
@user_passes_test(student_check, redirect_field_name=None)
def registerCourse(request):
    if request.method == "POST":
        student = request.user.student_data.get()
        courseForm = CourseForm(request.POST)
        if courseForm.is_valid():
            course = courseForm.cleaned_data["course"]
            studentsemester = StudentSemester.objects.filter(student=student,status=2).get()
            studentcourse = StudentCourse(student=student, course=course, semester=studentsemester)
            studentcourse.save()
            return HttpResponseRedirect(reverse("dashboard"))
    return render(request, "courses/registration.html", {
            "name": "Course",
            "formUrl": "registerCourse",
            "registrationForm": CourseForm()
        })