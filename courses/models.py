from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from university.models import Student, Teaching

class Department(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Degree(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="degrees_from_dept", default="")
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=64)
    credit_required = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Semester(models.Model):
    name = models.CharField(max_length=10)
    from_month = models.IntegerField()
    to_month = models.IntegerField()
    start = models.DateTimeField(default=datetime(2022,1,1))

    def __str__(self):
        return f"{self.name} {self.start.year}"

class Schedule(models.Model):
    name = models.CharField(max_length=3)
    monday = models.BooleanField(default=0)
    tuesday = models.BooleanField(default=0)
    wednesday = models.BooleanField(default=0)
    thursday = models.BooleanField(default=0)
    friday = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.name}"

#Status codes for various models
class Status(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

#Grade Scale to calculate SGPA
class Grade(models.Model):
    code = models.CharField(max_length=2)
    value = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.code} = {self.value}"

class Course(models.Model):

    #The below Foreign Key relatioship to the department model was made so that its easier to pull all courses in a particular department
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses_in_dept", default="") 

    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="courses_in_degree", default="")
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=64)
    credits = models.DecimalField(max_digits=2, decimal_places=1)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_DEFAULT, related_name="courses_on_schedule", default=0)
    semester_offered = models.ForeignKey(Semester, on_delete=models.SET_DEFAULT, related_name="courses_in_semester", default=0)

    def __str__(self):
        return f"{self.code} - {self.name}"


# A class to join Student and Degree to record enrollment and completion
class StudentDegree(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="degrees_of_student", default="")
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name="students_doing_degree", default="")
    credits_achieved = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, related_name="status_studentdegree", default="") #Applied/Enrolled/Completed/Dropped
    cgpa = models.DecimalField(max_digits=2, decimal_places=1)
    enrollment_date = models.DateTimeField(default=datetime.now)
    completed_date = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.student} - {self.degree} - {self.enrollment_date.year}"

    def serialize(self):
        return {
            "student": self.student.id,
            "degree": self.degree.name,
            "degreeCode": self.degree.code,
            "credits_achieved": self.credits_achieved,
            "status": self.status.name,
            "cgpa": self.cgpa
        }

#Storing Semester details for each student
class StudentSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="semester_student", default="")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="semester_studentsemester", default="")
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, related_name="status_studentsemester", default="") #Applied/Enrolled/Completed/Dropped
    sgpa = models.DecimalField(max_digits=2, decimal_places=1)
    enrollment_date = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.student} - {self.semester} - {self.enrollment_date.year}"

# A class to join Student and Course to record enrollment and completion
class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="courses_of_student", default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students_doing_course", default="")
    grade = models.ForeignKey(Grade, on_delete=models.SET_DEFAULT, related_name="students_with_grade", default="")
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, related_name="status_studentcourse", default="") #Applied/Enrolled/Completed/Failed/Dropped
    semester = models.ForeignKey(StudentSemester, on_delete=models.CASCADE, related_name="studentsemester_courses", default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.student} - {self.course}"
    
    def serialize(self):
        return {
            "semester" : self.semester,
            "course" : self.course
        }

#Storing which teacher is going to teach which course
class TeachingCourse(models.Model):
    teaching = models.ForeignKey(Teaching, on_delete=models.CASCADE, related_name="courses_of_teaching", default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="teching_course", default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.teaching} - {self.course}"

#Model to record the current time
class Current(models.Model):
    currentDateTime = models.DateTimeField()
    currentSemester = models.ForeignKey(Semester, on_delete=models.SET_DEFAULT, related_name="current_semeter", default="")

    def __str__(self):
        return f"{self.currentSemester} - {self.currentDateTime}"

#Model to record course content
class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_content", default="")
    description = models.TextField()
    lecture_url = models.URLField()
    notes = models.URLField()
    name = models.CharField(max_length=15)