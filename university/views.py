from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# User Tests
def admin_check(user):
    return user.user_type.code == "AD"

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
    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
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
        if user.user_type.code == "ST":
            user_data = user.student_data.get()
        elif user.user_type.code == "TE":
            user_data = user.teaching_data.get()
        elif user.user_type.code == "AD":
            user_data = user.admin_data.get()
        print(user.profile())
        if request.method == "POST":
            addressForm = AddressForm(request.POST)
            profileForm = UserProfileForm(request.POST,request.FILES)
            if addressForm.is_valid() and profileForm.is_valid():
                street = addressForm.cleaned_data["street"]
                apt = addressForm.cleaned_data["apt"]
                city = addressForm.cleaned_data["city"]
                pincode = addressForm.cleaned_data["pincode"]
                country = addressForm.cleaned_data["country"]
                state = addressForm.cleaned_data["state"]
                address = user_data.address
                address.street = street
                address.apt = apt
                address.city = city
                address.pincode = pincode
                address.country = country
                address.state = state
                photo = profileForm.cleaned_data["photo"]
                user.photo = photo
                bio = profileForm.cleaned_data["bio"]
                user.bio = bio
                print(user.bio)
                address.save()  
                user.save()
                return render(request, "university/editprofile.html", {
                    "addressForm": AddressForm(user_data.address.serialize()),
                    "profileForm": UserProfileForm(user.profile()),
                    "message": "Success"
                })

        return render(request, "university/editprofile.html", {
            "addressForm": AddressForm(user_data.address.serialize()),
            "profileForm": UserProfileForm(user.profile())
        })
    else:
        return render(request, "university/index.html")
    
@login_required    
@user_passes_test(admin_check, redirect_field_name=None)
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
            elif user.user_type.code == "AD":
                print("Admin")
                admin = UniversityAdmin(user=user, address=address)
                admin.save()
                group = Group.objects.get(name='University Admin')
                user.groups.add(group) 

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