from django.forms import ModelForm
from .models import *

class DegreeForm(ModelForm):
    class Meta:
        model = StudentDegree
        fields = ["degree"]


class CourseForm(ModelForm):
    class Meta:
        model = StudentCourse
        fields = ["course"]