from django.urls import path
from . import views

app_name = "coding"

urlpatterns = [
    path("", views.LearningPageView.as_view(), name="learn"),
    path("QuestionSelection/python/", views.pagepython, name="question_python"),
    path("QuestionSelection/cpp/", views.pagecpp, name="question_cpp"),
    path("QuestionSelection/java/", views.pagejava, name="question_java"),
    path("QuestionSelection/c/", views.pagec, name="question_c"),
    path("code", views.coding, name="coding")
]
