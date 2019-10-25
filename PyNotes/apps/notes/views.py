from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def index(request, id=None):
    if(id is None):
        user_id = request.user.id
        categories = Category.objects.filter(user=user_id)
        return render(request, 'notes/index.html', { 'categories' : categories, 'is_quill' : False })
    else:
        notes = Note.objects.filter(category=id)
        return render(request, 'notes/details.html', { 'notes' : notes, 'is_quill' : True })
