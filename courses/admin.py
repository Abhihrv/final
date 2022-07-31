from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('dept','code', 'name', 'credit_required')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('dept','code', 'name', 'credits', 'degree')

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name','from_month', 'to_month')

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student','course', 'grade', 'status')

class StudentDegreeAdmin(admin.ModelAdmin):
    list_display = ('student','degree', 'credits_achieved', 'status')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(StudentDegree, StudentDegreeAdmin)

