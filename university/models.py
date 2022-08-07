from django.contrib.auth.models import AbstractUser
from django.db import models

#Creating separate user type model to differentiate between different users of the site
class UserType(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

#Creating the first model to store users
class User(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name="users_of_type", default="")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Creating a separate model for defining genders
class Gender(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

#Creating a Address type field to store if Current or Home
class AddressType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

#Separate class for address
class Address(models.Model):
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE, related_name="address_of_type")
    street = models.CharField(max_length=128)
    apt = models.CharField(max_length=8)
    city = models.CharField(max_length=64)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.address_type}, {self.street}, {self.apt}, {self.city}, {self.pincode}, {self.country}, {self.state}"

    def serialize(self):
        return {
            "street": self.street,
            "apt": self.apt,
            "city": self.city,
            "pincode": self.pincode,
            "country": self.country,
            "state": self.state
        }    

#Creating model for designations
class Desgination(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

#Separate Model to store Student data
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_data")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="students_of_gender")
    address_home = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="students_at_home_address", default="")
    address_current = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="students_at_current_address", default="")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="students_in_designation")

    def __str__(self):
        return f"{self.user}"

#Separate Model for Teaching staff
class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teaching_data")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="teaching_in_designation")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="teaching_of_gender")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="teaching_at_address", default="")

    def __str__(self):
        return f"{self.user}"

#Separate Model for other staff
class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff_data")
    designation = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name="staff_in_designation")
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="staff_of_gender")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="staff_at_address", default="")

    def __str__(self):
        return f"{self.user}"
