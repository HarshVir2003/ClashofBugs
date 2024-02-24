from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import View
from coding.processing_coding import ProcessCodingData


@login_required(login_url="/login")
def dashboard(request, *args, **kwargs):
    process_class = ProcessCodingData()
    _, python_solved_questions = process_class.get_solved_question(User=request.user, Topic="python")
    _, cpp_solved_questions = process_class.get_solved_question(User=request.user, Topic="cpp")
    _, java_solved_questions = process_class.get_solved_question(User=request.user, Topic="java")
    _, c_solved_questions = process_class.get_solved_question(User=request.user, Topic="c")
    context = {
        "python": python_solved_questions,
        "cpp": cpp_solved_questions,
        "java": java_solved_questions,
        "c": c_solved_questions
        "user":request.user.username
    }

    return render(request, "dashboard.html", context)
