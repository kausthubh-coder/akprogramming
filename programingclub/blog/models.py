from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=False)
    content = HTMLField()