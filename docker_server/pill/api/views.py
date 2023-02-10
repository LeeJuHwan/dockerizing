from . import models
from .models import FileUpload
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
 
def upload_file(request):
    if request.method == "POST":
        user_file = request.FILES["인풋_파일업로드"]

        file_saving = models.FileUpload(
            save_files = user_file
        )
        file_saving.save()
        file_path = file_saving.save_files

    image_query = get_object_or_404(FileUpload, save_files = file_path)

    user_id = image_query.id
    return HttpResponseRedirect(reverse('api:result', args=(user_id,)))

def show_image(request, user_id):
    image_info = get_object_or_404(FileUpload, id=user_id)
    context = {'정보': image_info}
    return render(request, 'api/result.html', context)
