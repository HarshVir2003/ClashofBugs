from django.db import models
from django.conf import settings
import uuid



class Certificate(models.Model):
    Title = models.CharField(max_length=256)
    topic = models.CharField(max_length=64)


class CertificateUser(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Attained = models.BooleanField(default=False)
    UID = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.UID:
            self.UID = uuid.uuid4().hex
        super().save(*args, **kwargs)


class Tournament(models.Model):
    Title = models.CharField(max_length=128)
    Photo = models.CharField(max_length=256)
    StartDate = models.DateField()
    EndDate = models.DateField(default=None)
    Description = models.TextField()
    MinLevel = models.IntegerField()
    MaxLevel = models.IntegerField()
    Reward1 = models.CharField(max_length=32)
    Reward2 = models.CharField(max_length=32)
    Reward3 = models.CharField(max_length=32)


class TournamentUser(models.Model):
    Tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    participated = models.BooleanField(default=False)
