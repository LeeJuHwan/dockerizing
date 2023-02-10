from django.db import models
 
class FileUpload(models.Model) :
    save_files = models.FileField(upload_to='Uploaded Files/%y/%m/%d/', blank=True)
    pub_date = models.DateField(auto_now = True)
