from django.db import models
from django.db.models.fields import DateField

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField
    newwork = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)