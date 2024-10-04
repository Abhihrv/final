from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from .models import *

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ["street", "apt", "city", "state", "country", "pincode"]

class UserForm(UserCreationForm):

    # user_type = forms.ChoiceField(choices=UserType.objects.all().values_list('code', 'name'))
    class Meta:
      model = User
      fields = ["username", "password1", "password2", "first_name", "last_name", "email", "user_type"]