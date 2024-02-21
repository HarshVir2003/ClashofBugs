from django.db import models
from coding.models import CodingQuestions
from django.contrib.auth import get_user_model
import uuid


# Create your models here.
class UserMatching(models.Model):
    User = get_user_model()
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usermatching_user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usermatching_user2")
    question = models.ForeignKey(CodingQuestions, on_delete=models.CASCADE)
    url = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.url:
            self.UID = uuid.uuid4().hex
        super().save(*args, **kwargs)


class ButtonClick(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    matched = models.BooleanField(default=False)
