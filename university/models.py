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

#Separate class for address
class Address(models.Model):
    street = models.CharField(max_length=128)
    apt = models.CharField(max_length=8, blank=True)
    city = models.CharField(max_length=64)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.street}, {self.apt}, {self.city}, {self.pincode}, {self.country}, {self.state}"

    def serialize(self):
        return {
            "street": self.street,
            "apt": self.apt,
            "city": self.city,
            "pincode": self.pincode,
            "country": self.country,
            "state": self.state
        }    

#Separate Model to store Student data
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_data")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address", default="")

    def __str__(self):
        return f"{self.user} - {self.address}"

#Separate Model for Teaching staff
class Teaching(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teaching_data")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="teaching_at_address", default="")

    def __str__(self):
        return f"{self.user}"