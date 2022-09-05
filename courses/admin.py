from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('dept','code', 'name', 'credit_required')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('dept','code', 'name', 'credits', 'degree', 'semester_offered')

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name','from_month', 'to_month', 'start')

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student','course', 'semester', 'grade', 'status')

class StudentDegreeAdmin(admin.ModelAdmin):
    list_display = ('student','degree', 'credits_achieved', 'status', 'cgpa')

class StudentSemesterAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'created', 'updated', 'enrollment_date')

class TeachingCourseAdmin(admin.ModelAdmin):
    list_display = ('teaching', 'course', 'created', 'updated')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('code', 'value')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class CurrentAdmin(admin.ModelAdmin):
    list_display = ('currentDateTime', 'currentSemester')

class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('course', 'description', 'lecture_url', 'notes', 'name')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(StudentDegree, StudentDegreeAdmin)
admin.site.register(StudentSemester, StudentSemesterAdmin)
admin.site.register(TeachingCourse, TeachingCourseAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Current, CurrentAdmin)
admin.site.register(CourseContent, CourseContentAdmin)

