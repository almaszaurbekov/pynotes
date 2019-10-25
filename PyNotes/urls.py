from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # index
    path('', views.index, name='index'),
    # admin
    path('admin/', admin.site.urls),
    # login
    path('accounts/', include('django.contrib.auth.urls')),
    # register
    path('register/', views.register, name='register'),
    # categories
    path('categories/', include('notes.urls')),
    # categories/2/notes/
    # path('categories/<int:id>/notes/', include('notes.urls'))
    # path('notes/<int:id>', include('notes.urls')),
    # path('notes/create', include('notes.urls'))
]