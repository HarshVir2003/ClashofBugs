from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Tournament, TournamentUser
from django.views.decorators.csrf import csrf_protect
from .forms import MyForm
from .processing_tournament import ProcessTournamentData
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def getpage(request):
    data_object = ProcessTournamentData()
    on_going, upcoming, participated = data_object.get_status(request.user)
    first_element_on = 0
    first_element_up = 0
    first_element_par = 0
    if on_going:
        first_element_on = on_going[0]
    if upcoming:
        first_element_up = upcoming[0]
    if participated:
        first_element_par = participated[0]

    if request.method == "POST":
        tourna = Tournament.objects.get(id=request.POST.get('register'))
        tu = TournamentUser.objects.create(Tournament=tourna, user=request.user, participated=True)
        tu.save()
        # return HttpResponse(TournamentUser.objects.all())
        return render(request, "tournament.html",
                      {"on_going": on_going,
                       "upcoming": upcoming,
                       "participated": participated,
                       "first_on": first_element_on,
                       "first_up": first_element_up,
                       "first_par": first_element_par})
    else:
        return render(request, "tournament.html",
                      {"on_going": on_going,
                       "upcoming": upcoming,
                       "participated": participated,
                       "first_on": first_element_on,
                       "first_up": first_element_up,
                       "first_par": first_element_par})
