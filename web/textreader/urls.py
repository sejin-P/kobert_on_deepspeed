from django.urls import path
from . import views

app_name = 'textreader'

urlpatterns = [
    path('',views.index, name='index'),
    path('uploader/<int: uploader_id>', views.show_text, name='show_text')
]