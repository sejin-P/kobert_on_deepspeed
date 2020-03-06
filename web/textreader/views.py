from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .user import handle_uploaded_file, upload_text_from_file
from .user import UploadFileForm
from .models import Uploader, Text


def index(request):
    return HttpResponse("Django project with Docker")


def show_text(request, uploader_id):
    uploader = get_object_or_404(Uploader, pk=uploader_id)
    text_li = uploader.text_set.all()
    return render(request, 'text_reader/user_text.html', {'uploader': uploader, 'text_li': text_li)


def upload_file(request, uploader_id):
    uploader = get_object_or_404(Uploader, pk=uploader_id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload_text_from_file(uploader, form)
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/') #TODO: Link where?
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def upload_text(request, uploader_id):
    uploader = get_object_or_404(Uploader, pk=uploader_id)
    if request.method == 'POST':
        text = request.POST['text']
        Text.create(uploader = uploader, text=text)
        return HttpResponseRedirect('/success/url')
    else:
        return HttpResponseRedirect('text_reader/')


