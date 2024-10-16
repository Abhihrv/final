from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

#Main index view for the site
@login_required
def index(request):
    return render(request, "university/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "university/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "university/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def profile(request, username):
    user = User.objects.get(username = username)
    return render(request, "university/profile.html", {
        "user" : user
    })

@login_required
def editprofile(request, username):
    user = User.objects.get(username = username)
    if user == request.user:
        if request.method == "POST":
            formAddress = AddressForm(request.POST)
            if formAddress.is_valid():
                street = formAddress.cleaned_data["street"]
                apt = formAddress.cleaned_data["apt"]
                city = formAddress.cleaned_data["city"]
                pincode = formAddress.cleaned_data["pincode"]
                country = formAddress.cleaned_data["country"]
                state = formAddress.cleaned_data["state"]
                student_data = user.student_data.get()
                student_data.save()
                address = student_data.address
                address.street = street
                address.apt = apt
                address.city = city
                address.pincode = pincode
                address.country = country
                address.state = state
                address.save()
        return render(request, "university/editprofile.html", {
            "formAddress": AddressForm()
        })
    else:
        return render(request, "university/index.html")
    
@login_required    
def register(request):
    if request.method == "POST" and request.user.has_perm('university.add_user'):
        userForm = UserForm(request.POST)
        addressForm = AddressForm(request.POST)
        if userForm.is_valid() and addressForm.is_valid():
            addressForm.save()
            userForm.save()
            user = User.objects.filter(username=userForm.cleaned_data["username"]).get()
            address = Address.objects.filter(street=addressForm.cleaned_data["street"]).get()
            if user.user_type.code == "ST":
                student = Student(user=user, address=address)
                student.save()
            elif user.user_type.code == "TE":
                print("teaching")
                teaching = Teaching(user=user, address=address)
                teaching.save()
            return render(request, "university/register.html", {
                    "message": "User Added!",
                    "success": True,
                    "userForm": UserForm(),
                    "addressForm": AddressForm()
                })
        else:
            return render(request, "university/register.html", {
                    "message": "Invalid Form!",
                    "success": False,
                    "userForm": userForm,
                    "addressForm": addressForm
                })
    elif request.user.has_perm('university.add_user'):         
        return render(request, "university/register.html", {
            "userForm": UserForm(),
            "addressForm": AddressForm()
        })
    else:
        return HttpResponseRedirect(reverse("index"))