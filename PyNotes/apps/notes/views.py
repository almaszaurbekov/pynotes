from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def index(request):
    return render(request, 'notes/index.html')