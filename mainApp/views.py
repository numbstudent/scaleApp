from mainApp.forms import *
from mainApp.models import *
from django.shortcuts import get_list_or_404, render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import RestrictedError, Sum, Q, F
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required
from django import template
register = template.Library()

loginpage = 'login'

@login_required(login_url=loginpage)
def index(request):
    return render(request,'home.html')
