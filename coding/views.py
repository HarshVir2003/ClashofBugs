import time

from django.middleware.csrf import get_token
from django.shortcuts import render, HttpResponse, redirect
from .processing_coding import ProcessCodingData
from .models import CodingQuestions, TestCases, ProblemStatus
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .judgement import submission, get_status, languages


# Create your views here.
@method_decorator(login_required(login_url="/login"), name='get')
class LearningPageView(View):
    template_name = "coding/selection.html"

    # @login_required(login_url="/login")

    def get(self, request, *args, **kwargs):
        process_class = ProcessCodingData()
        _, python_solved_questions = process_class.get_solved_question(User=request.user, Topic="python")
        _, cpp_solved_questions = process_class.get_solved_question(User=request.user, Topic="cpp")
        _, java_solved_questions = process_class.get_solved_question(User=request.user, Topic="java")
        _, c_solved_questions = process_class.get_solved_question(User=request.user, Topic="c")
        context = {
            "csrf_token": get_token(request),
            "python": python_solved_questions,
            "cpp": cpp_solved_questions,
            "java": java_solved_questions,
            "c": c_solved_questions
        }
        return render(request, self.template_name, context)


# @method_decorator(login_required(login_url="/login"), name='get')
# class QuestionPageView(View):
#     template_name = "coding/question_selection.html"
#
#     # @login_required(login_url="/login")
#     def get(self, request, *args, **kwargs):
#         data_object = CodingQuestions
#         PROBLEM_HARDNESS_CHOICES = ['easy', 'medium', 'hard']
#         data_object = data_object.objects.filter(topic="python")
#
#         level_values = [PROBLEM_HARDNESS_CHOICES[i.problem_hardness] for i in data_object]
#
#         context = {
#             'python': zip(data_object, level_values),  # Pair each question with its level
#         }
#         if request.method == 'POST':
#             data = request.POST.get('id')
#             return HttpResponse(data)
#         else:
#             # return HttpResponse('no')
#             return render(request, self.template_name, context)
@login_required(login_url='/login')
def pagepython(request, *args, **kwargs):
    data_object = CodingQuestions
    PROBLEM_HARDNESS_CHOICES = ['easy', 'medium', 'hard']
    data_object = data_object.objects.filter(topic="python")

    level_values = [PROBLEM_HARDNESS_CHOICES[i.problem_hardness] for i in data_object]

    context = {
        'python': zip(data_object, level_values),  # Pair each question with its level
    }
    if request.method == 'POST':
        data = request.POST.get('questionbtn')
        request.session['data'] = data
        return redirect('/learn/code')
    else:
        # return HttpResponse('no')
        return render(request, "coding/question_selection.html", context)


@login_required(login_url='/login')
def pagecpp(request, *args, **kwargs):
    data_object = CodingQuestions
    PROBLEM_HARDNESS_CHOICES = ['easy', 'medium', 'hard']
    data_object = data_object.objects.filter(topic="cpp")

    level_values = [PROBLEM_HARDNESS_CHOICES[i.problem_hardness] for i in data_object]

    context = {
        'python': zip(data_object, level_values),  # Pair each question with its level
    }
    if request.method == 'POST':
        data = request.POST.get('questionbtn')
        request.session['data'] = data
        return redirect('/learn/code')
    else:
        # return HttpResponse('no')
        return render(request, "coding/question_selection.html", context)


@login_required(login_url='/login')
def pagejava(request, *args, **kwargs):
    data_object = CodingQuestions
    PROBLEM_HARDNESS_CHOICES = ['easy', 'medium', 'hard']
    data_object = data_object.objects.filter(topic="java")

    level_values = [PROBLEM_HARDNESS_CHOICES[i.problem_hardness] for i in data_object]

    context = {
        'python': zip(data_object, level_values),  # Pair each question with its level
    }
    if request.method == 'POST':
        data = request.POST.get('questionbtn')
        request.session['data'] = data
        return redirect('/learn/code')
    else:
        # return HttpResponse('no')
        return render(request, "coding/question_selection.html", context)


@login_required(login_url='/login')
def pagec(request, *args, **kwargs):
    data_object = CodingQuestions
    PROBLEM_HARDNESS_CHOICES = ['easy', 'medium', 'hard']
    data_object = data_object.objects.filter(topic="c")

    level_values = [PROBLEM_HARDNESS_CHOICES[i.problem_hardness] for i in data_object]

    context = {
        'python': zip(data_object, level_values),  # Pair each question with its level
    }
    if request.method == 'POST':
        data = request.POST.get('questionbtn')
        request.session['data'] = data
        return redirect('/learn/code')
    else:
        # return HttpResponse('no')
        return render(request, "coding/question_selection.html", context)


@login_required(login_url='/login')
def coding(request):
    data = request.session.get('data', None)
    question = CodingQuestions.objects.get(id=data)
    input_question = question.input_example.split('/n')
    output = question.output_example.split('/n')
    compiler_message = "-"
    stdin = "-"
    stdout = "-"
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
        test_cases = TestCases.objects.filter(key=CodingQuestions.objects.get(id=data))
        results = []
        test = []
        x = 1
        for i in test_cases:
            a = submission(str(request.POST.get('code')), str(request.POST.get('lang')), languages,
                           stdin=str(i.test_case_input),
                           stdout=str(i.test_case_output))

            time.sleep(1)
            a = get_status(a.get('token'))
            test.append(x)
            x += 1

            results.append([a.get('stdout'), i.test_case_input, a.get('time')])
        qs = ProblemStatus.objects.get(user=request.user, question=question)
        return render(request, 'coding/learning_page.html',
                      {'question': question, 'input_q': input_question, 'output_q': output,
                       "result": results, 'test': test, "pre": qs})

    else:
        return render(request, 'coding/learning_page.html',
                      {'question': question, 'input_q': input_question, 'output_q': output,
                       "compiler_message": compiler_message, "stdin": stdin, "stdout": stdout})
