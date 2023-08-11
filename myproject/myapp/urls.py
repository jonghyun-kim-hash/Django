from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
   path('', views.index),
   path('create/', views.create),
   path('read/<id>', views.read),
]
