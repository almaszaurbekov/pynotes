from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from .models import *

# Create your views here.
def index(request, user_id):
    try:
        notes = Note.objects.get( user_id = user_id )
    except:
        notes = [{ "id" : 1, "text" : "Hello world!"}, { "id" : 2, "text" : "This is so cool!"}, { "id" : 3, "text" : "I love Django!"}]
        return render(request, 'notes/index.html', { 'notes' :  notes })

    return render(request, 'notes/index.html', { 'notes' : notes })

def details(request, note_id):
    notes = [{ "id" : 1, "text" : "Hello world!"}]
    return render(request, 'notes/index.html', { 'notes' : notes })