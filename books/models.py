from django.db import models

# Create your models here.
class Author(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
