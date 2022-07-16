from django.shortcuts import render
from .models import *

# Create your views here.

#Main index view for the site
def index(request):
    return render(request, "university/index.html")
