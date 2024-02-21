from django.db import models
from django.conf import settings


# Create your models here.
class CodingQuestions(models.Model):
    PROBLEM_HARDNESS_CHOICES = (
        (0, 'easy'),
        (1, 'medium'),
        (2, 'hard')
    )
    title = models.TextField()
    primary_text = models.TextField(unique=True)
    input_text = models.CharField(max_length=2000)
    output_text = models.CharField(max_length=2000)
    input_example = models.CharField(max_length=1024)
    output_example = models.CharField(max_length=1024)
    topic = models.CharField(max_length=100)
    xp = models.IntegerField()
    problem_hardness = models.IntegerField(
        choices=PROBLEM_HARDNESS_CHOICES,
        default=0
    )

    def __str__(self):
        return f"{self.primary_text}"


class ProblemStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(CodingQuestions, on_delete=models.CASCADE)
    solution = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.question.primary_text}"


class TestCases(models.Model):
    key = models.ForeignKey(CodingQuestions, on_delete=models.CASCADE)
    test_case_input = models.TextField()
    test_case_output = models.TextField()

    def __str__(self):
        return f"{self.key.primary_text}"


