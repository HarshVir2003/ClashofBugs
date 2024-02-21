from django.contrib.auth import get_user_model
from tournaments.models import TournamentUser, Tournament

class ProcessUserData:
    # User = get_user_model()

    def get_level_exp(self, player_xp):
        level = 1
        xp_required = 100  # Initial XP required for level 1
        while level < 100:
            if level % 10 == 0:
                xp_required = 800  # For levels divisible by 10
            if player_xp >= xp_required:
                player_xp -= xp_required
                level += 1
                if level % 10 != 0:
                    xp_required += 400  # Increase XP required by 400 until the next level divisible by 10
            else:
                break

        if level < 100:
            xp_to_next_level = xp_required - player_xp
        else:
            xp_to_next_level = 0

        return level, xp_to_next_level


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


class CodingData:
    ...


class CertificateData:
    ...


