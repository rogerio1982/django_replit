from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to ='static/',blank=True)
