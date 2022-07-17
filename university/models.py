from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

#Creating separate user type model to differentiate between students and teachers
class UserType(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=64)

#Creating the first model to store users
class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, related_name="users_of_type", default="")

#Creating a separate model for defining genders
class Gender(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=64)

#Creating a Address type field to store if Current or Home
class AddressType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=64)

#Separate class for address
class Address(models.Model):
    street = models.CharField(max_length=128)
    apt = models.CharField(max_length=8)
    city = models.CharField(max_length=64)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=64)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE, blank=True, related_name="address_of_type")
    state = models.CharField(max_length=64)

#Creating model for designations
class Desgination(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=64)

#Separate Model to store Student data
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_data")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, related_name="students_of_gender")
    address_home = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, related_name="students_at_home_address", default="")
    address_current = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, related_name="students_at_current_address", default="")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="students_in_designation")

#Separate Model for Teaching staff
class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teaching_data")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="teaching_in_designation")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, related_name="teaching_of_gender")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, related_name="teaching_at_address", default="")

#Separate Model for other staff
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff_data")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="staff_in_designation")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, related_name="staff_of_gender")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, related_name="staff_at_address", default="")
