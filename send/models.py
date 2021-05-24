from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class post(models.Model):
    body = RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        return self.body
    

    