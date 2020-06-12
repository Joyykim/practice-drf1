from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Card(models.Model):
    created_at = models.DateTimeField()
    content = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='cards', on_delete=models.CASCADE)
    is_reported = models.BooleanField(default=False)
    title = models.CharField(max_length=128, default='title~!')