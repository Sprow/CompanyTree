from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from utils import get_file_path


class User(AbstractUser):
    parent_id = models.PositiveIntegerField(null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True, default=timezone.now())
    salary = models.PositiveIntegerField(null=True, blank=True)
    position = models.CharField(max_length=100)
    photo = models.FileField(upload_to=get_file_path, blank=True, null=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
