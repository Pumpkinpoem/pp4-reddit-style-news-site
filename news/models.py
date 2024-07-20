from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = SummernoteTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title