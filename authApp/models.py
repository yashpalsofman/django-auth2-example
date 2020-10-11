from django.db import models
from django.contrib.auth.models import User as BaseUser


class User(models.Model):
    base_user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name="local_users")
    user_type = models.CharField(max_length=255, default="read write update delete")
