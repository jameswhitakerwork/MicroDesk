from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from .models import *

# Create your views here.


def index(request):
    messages.success(request, "You are logged in!")
    messages.warning(request, "But this app is not ready yet...")
    return render(request, 'hr/index.html', {})


def contact_list(request):
    # searchable list of contacts
    pass


def staff_profile(request):
    pass


class Contact_List(ListView):
    model = Staff
