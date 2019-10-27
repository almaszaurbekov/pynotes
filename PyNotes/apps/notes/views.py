from django.shortcuts import render, redirect
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

@login_required
def categories(request):
    user_id = request.user.id
    categories = Category.objects.filter(user=user_id)
    return render(request, 'notes/categories.html', { 'categories' : categories })

@login_required
def categoryById(request, category_id):
    category = Category.objects.get(id=category_id)
    notes = Note.objects.filter(category=category_id)
    return render(request, 'notes/notes.html', { 'notes' : notes, 'category' : category })

@login_required
def noteById(request, category_id, note_id, is_success=None):
    category = Category.objects.get(id=category_id)
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/note.html', { 'note' : note, 'category' : category, 'is_success' : is_success })

@login_required
def createCategory(request):
    if request.method == 'GET':
        colors = Color.objects.all()
        return render(request, 'notes/createCategory.html', {'colors' : colors, 'user' : request.user })
    else:
        name = request.POST.get('name')
        color = Color.objects.get(id=request.POST.get('color'))
        instance = Category.objects.create(name=name, color=color, user=request.user)
        return redirect('categories')

@login_required
def deleteCategory(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        notes = Note.objects.filter(category=category_id)
        return render(request, 'notes/deleteCategory.html', { 'notes' : notes, 'category' : category })
    else:
        category = Category.objects.filter(id=category_id).delete()
        return redirect('categories')

@login_required
def createNote(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        return render(request, 'notes/createNote.html', {'category' : category, 'user' : request.user })
    else:
        title = request.POST.get('title')
        category = Category.objects.get(id=request.POST.get('category'))
        instance = Note.objects.create(title=title, text='', category=category, user=request.user)
        return redirect('categoryById', category_id=request.POST.get('category'))

@login_required
def deleteNote(request, category_id, note_id, is_success):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/deleteNote.html', { 'note' : note, 'category' : category })
    else:
        category = Category.objects.get(id=category_id)
        note = Note.objects.filter(id=note_id).delete()
        return redirect('categoryById', category_id=category_id)

@login_required
def quillText(request):
    if request.method == 'POST':
        quill = request.POST.get('quillData')

        category_id = request.POST.get('category')

        note_id = request.POST.get('note')
        note = Note.objects.filter(id=note_id);

        instance = note.update(text=quill)
        return redirect('noteById', category_id, note_id, True)