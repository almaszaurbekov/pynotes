from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>/notes/', views.categoryById, name='categoryById'),
    path('<int:category_id>/notes/<int:note_id>/<is_success>', views.noteById, name='noteById'),
    path('create/', views.createCategory, name='createCategory'),
    path('<int:category_id>/delete/', views.deleteCategory, name='deleteCategory'),
    path('<int:category_id>/notes/create/', views.createNote, name='createNote'),
    path('<int:category_id>/notes/<int:note_id>/<is_success>/delete', views.deleteNote, name='deleteNote'),
    path('quillText/', views.quillText, name='quillText')
]