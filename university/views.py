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

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "university/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email, password=password, user_type=UserType.objects.get(code='ST'))
            user.save()
        except IntegrityError:
            return render(request, "university/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "university/register.html")

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
            formStudent = StudentForm(request.POST)
            formAddress = StudentAddressForm(request.POST)
            if formStudent.is_valid() and formAddress.is_valid():
                gender = formStudent.cleaned_data["gender"]
                street = formAddress.cleaned_data["street"]
                apt = formAddress.cleaned_data["apt"]
                city = formAddress.cleaned_data["city"]
                pincode = formAddress.cleaned_data["pincode"]
                country = formAddress.cleaned_data["country"]
                state = formAddress.cleaned_data["state"]
                student_data = user.student_data.get()
                student_data.gender = gender
                student_data.save()
                address = student_data.address_home
                address.street = street
                address.apt = apt
                address.city = city
                address.pincode = pincode
                address.country = country
                address.state = state
                address.save()
        return render(request, "university/editprofile.html", {
            "formStudent": StudentForm(initial= {"gender": user.student_data.get().gender}),
            "formAddress": StudentAddressForm(initial= user.student_data.get().address_home.serialize())
        })
    else:
        return render(request, "university/index.html")