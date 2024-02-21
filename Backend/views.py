import random
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from battle.models import UserMatching, ButtonClick
from coding.judgement import submission, get_status, languages
from django.db.models import Q
from django.contrib.auth import get_user_model
import uuid
from coding.models import CodingQuestions, ProblemStatus, TestCases
from django.contrib.auth.decorators import login_required
import time
from django.views.decorators.csrf import csrf_exempt
from dashboard.processing_dashboard import ProcessUserData


def win(request):
    user = get_user_model()
    button_clicker = ButtonClick.objects.filter(user=user).first()
    if button_clicker:
        button_clicker.delete()

    # Delete UserMatching object
    user_matching = UserMatching.objects.filter(Q(user1=user) | Q(user2=user)).first()
    if user_matching:
        user_matching.delete()
    return render(request, 'backend/win.html')


def lose(request):
    user = get_user_model()
    button_clicker = ButtonClick.objects.filter(user=user).first()
    if button_clicker:
        button_clicker.delete()

    # Delete UserMatching object
    user_matching = UserMatching.objects.filter(Q(user1=user) | Q(user2=user)).first()
    if user_matching:
        user_matching.delete()
    return render(request, 'backend/lose.html')
