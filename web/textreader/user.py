from django import forms
from .models import Text

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_text_from_file(uploader, form):
    file = form.file
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            category = line.split('\t')[0]
            text = line.split('\t')[1]
            Text.create(uploader=uploader, text=text, category=category)

