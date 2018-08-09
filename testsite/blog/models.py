from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib


class User(AbstractUser):
    uid = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        uid = hashlib.md5((self.username + self.email).encode()).hexdigest()
        self.uid = uid
        super(User, self).save(*args, **kwargs)
