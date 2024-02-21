from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    xp = models.IntegerField(default=0)
    trophies = models.IntegerField(default=0)
    UID = models.CharField(max_length=100, unique=True)
    Avatar = models.CharField(max_length=24)

    def save(self, *args, **kwargs):
        if not self.UID:
            self.UID = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)
        super().clean()
