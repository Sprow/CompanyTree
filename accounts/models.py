from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    parent_id = models.PositiveIntegerField(null=True)
    date_joined = models.DateField(blank=True, null=True)
    salary = models.PositiveIntegerField()
    position = models.CharField(max_length=255)
    # photo = models.FileField(upload_to=get_file_path)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
