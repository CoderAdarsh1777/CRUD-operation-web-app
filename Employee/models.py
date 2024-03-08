from django.db import models
from tinymce.models import HTMLField
class Employees(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100)
    address = HTMLField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
