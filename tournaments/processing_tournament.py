from .models import TournamentUser, Tournament
from dashboard.processing_dashboard import ProcessUserData
from datetime import date


class ProcessTournamentData:

    def register_user(self, User, tournament_id):
        tournament = Tournament.objects.get(id=tournament_id)
        tournament_user = TournamentUser.objects.create(Tournament=tournament, User=User, participated=True)
        tournament_max_level = tournament.MaxLevel
        tournament_min_level = tournament.MinLevel
        GetLevel = ProcessUserData()
        level, _ = GetLevel.get_level_exp(User)
        if (level <= tournament_max_level) and (level >= tournament_min_level):
            tournament_user.save()
            return f"You have Registered !"
        else:
            return f"You cannot Register !"

    def get_status(self, user):
        ongoing = []
        upcoming = []
        for i in Tournament.objects.all():
            s = i.StartDate
            e = i.EndDate
            today = date.today()
            if s <= today:
                ongoing.append(i)
            elif s > today:
                upcoming.append(i)

        participated_user = TournamentUser.objects.filter(user=user)
        participated = [i.Tournament for i in participated_user if i.participated]

        ongoing = [i for i in ongoing if i not in participated]
        upcoming = [i for i in upcoming if i not in participated]


        return ongoing, upcoming, participated
