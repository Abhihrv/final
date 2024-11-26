from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('degree', views.degree, name='mydegree'),
    path('degree/<int:degree_id>', views.getDegree, name='getDegree'),
    path('degree/register', views.registerDegree, name='registerDegree'),
    path('<str:course_code>', views.course, name='course'),
    path('course/register', views.registerCourse, name='registerCourse')
]