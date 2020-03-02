from django.urls import path
from . import views

app_name = 'textreader'

urlpatterns = [
    path('',views.index, name='index')
]