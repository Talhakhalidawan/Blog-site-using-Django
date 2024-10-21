from django.core.exceptions import ValidationError
from django.db import models
import os

# Create your models here.

class Post(models.Model):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1].lower()

        if ext not in ["jpg", "png", "gif", "jpeg"]:
            raise ValidationError(f"invalid image extension: {filename}")

        if instance.pk:
            filename = f"{instance.pk}, {ext}"
        else:
            filename = f"{filename}.{ext}"
        return os.path.join("Post-Images", filename)
    
    uid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100 , blank = True)
    upImageCaption = models.TextField()
    downImageCaption = models.TextField()
    date = models.BooleanField(default = False)
    image = models.ImageField(upload_to = "Post-Images" , blank = True)
    dateCreated = models.DateTimeField(auto_now_add = True)