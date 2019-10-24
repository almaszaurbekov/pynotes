from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.index, name='index'),
    path('<int:note_id>/details', views.details, name='details'),
]