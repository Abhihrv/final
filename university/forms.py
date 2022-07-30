from django import forms
from django.forms import ModelForm
from .models import *

#Form to edit profile
# class EditStudentProfileForm(ModelForm):
#     username = forms.CharField(label="Username", initial="Username")
#     gender = forms.ChoiceField(choices=list(Gender.objects.values_list("code", "name")))
#     home_street = forms.CharField(label="Street Name", initial="Street Name", max_length=128)
#     home_apt = forms.CharField(label="Apartment Name", initial="Apartment Name", max_length=8)
#     home_city = forms.CharField(label="City", initial="City", max_length=64)
#     home_pincode = forms.CharField(label="Pincode", initial="Pincode", max_length=10)
#     home_country = forms.CharField(label="Country", initial="Country", max_length=64)
#     home_state = forms.CharField(label="State", initial="State", max_length=64)
#     current_street = forms.CharField(label="Street Name", initial="Street Name", max_length=128)
#     current_apt = forms.CharField(label="Apartment Name", initial="Apartment Name", max_length=8)
#     current_city = forms.CharField(label="City", initial="City", max_length=64)
#     current_pincode = forms.CharField(label="Pincode", initial="Pincode", max_length=10)
#     current_country = forms.CharField(label="Country", initial="Country", max_length=64)
#     current_state = forms.CharField(label="State", initial="State", max_length=64)

class StudentAddressForm(ModelForm):
    address_type = forms.ChoiceField(choices=AddressType.objects.filter(name__in = ["current", "home"]).values_list())
    class Meta:
        model = Address
        exclude = ["address_type"]

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ["user", "age", "address_home", "address_current", "designation"]