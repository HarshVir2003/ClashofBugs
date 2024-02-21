import random
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from .models import UserMatching, ButtonClick
from coding.judgement import submission, get_status, languages
from django.db.models import Q
import uuid
from coding.models import CodingQuestions, ProblemStatus, TestCases
from django.contrib.auth.decorators import login_required
import time
from django.views.decorators.csrf import csrf_exempt
from dashboard.processing_dashboard import ProcessUserData


@csrf_exempt
def get_updated_value(request):
    match = ""
    button_clicker = ButtonClick.objects.create(user=request.user)

    while True:
        unmatched_users = ButtonClick.objects.filter(matched=False).exclude(id=button_clicker.id)
        if button_clicker.matched == False and unmatched_users.exists():
            matched_user = random.choice(unmatched_users)
            button_clicker.matched = True
            button_clicker.save()
            matched_user.matched = True
            matched_user.save()

            # Create a unique URL for the match
            match_url = uuid.uuid4().hex[:10]
            question = random.choice(CodingQuestions.objects.filter(topic="battle"))
            # Create UserMatching entry
            match = UserMatching.objects.create(user1=request.user, user2=matched_user.user, url=match_url,
                                                question=question)

            # Wait for the other user to click the button
            while True:
                user_match = UserMatching.objects.filter(Q(user1=request.user) | Q(user2=request.user)).first()
                if user_match:
                    updated_a = user_match.url
                    return JsonResponse({'a': updated_a})

        else:
            # Check if another user created the match
            user_match = UserMatching.objects.filter(Q(user1=request.user) | Q(user2=request.user)).first()
            if user_match:
                updated_a = user_match.url
                return JsonResponse({'a': updated_a})

            time.sleep(1)  # Sleep for a short duration before checking again



# Create your views here.
@login_required(login_url="/login")
def index(request):
    data_object = ProcessUserData()
    data, next, percentage_acquired = data_object.get_level_exp(request.user.xp)
    data_r, next_r, percentage_acquired_r = data_object.get_rank_exp(request.user.trophies)
    medal = {
        1: ["Bug Catcher", ""],
        2: ["Debugger", ""],
        3: ["BugBuster", ""],
        4: ["Bug Marshal", ""],
        5: ["Bug Exterminator", ""]
    }

    # return HttpResponse(f"level{data}, xp req{next}, acq{percentage_acquired}")
    return render(request, "find.html", {'per': percentage_acquired, "req": next, "lev": data, 'next_r': next_r,
                                         'per_r': percentage_acquired_r, 'rank': medal.get(data_r)[0]})


@login_required(login_url="/login")
def room(request, room_name):
    username = request.user.username
    user_match = UserMatching.objects.filter(Q(user1=request.user) | Q(user2=request.user)).first()
    question = user_match.question

    input_question = question.input_example.split('/n')
    output = question.output_example.split('/n')

    if request.method == "POST":
        request.user.xp = request.user.xp + question.xp
        request.user.save()
        try:
            qs = ProblemStatus.objects.get(user=request.user, question=question)
            qs.solution = request.POST.get('code')
            qs.save()
        except:
            qs = ProblemStatus.objects.create(user=request.user, question=question, solution=request.POST.get('code'))
            qs.save()
        test_cases = TestCases.objects.filter(key=CodingQuestions.objects.get(id=user_match.question.id))
        results = []
        test = []
        x = 1
        re_data = 0
        for i in test_cases:
            a = submission(str(request.POST.get('code')), str(request.POST.get('lang')), languages,
                           stdin=str(i.test_case_input),
                           stdout=str(i.test_case_output))

            time.sleep(1)
            a = get_status(a.get('token'))
            test.append(x)
            x += 1
            try:
                if (a.get("stdout") in i.test_case_output) or (i.test_case_output in a.get("stdout")):
                    re_data += 1
                else:
                    pass
            except:
                pass

            results.append([a.get('stdout'), i.test_case_input, a.get('time')])
        qs = ProblemStatus.objects.get(user=request.user, question=question)
        win = 0
        if re_data == len(test_cases):
            win = 1
        else:
            pass
        if win:
            return redirect('/win')
        else:
            return render(request, 'battle/battle.html',
                      {'question': question, 'input_q': input_question, 'output_q': output,
                       "result": results, 'test': test, "pre": qs, "win": win})
    else:
        return render(request, "battle/battle.html",
                      {"room_name": room_name, "username": username, 'question': question, 'input_q': input_question,
                       'output_q': output})
