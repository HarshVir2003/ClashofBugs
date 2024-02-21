from django.contrib.auth import get_user_model


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
            percentage_acquired = (1 - (xp_to_next_level / xp_required)) * 100
        else:
            xp_to_next_level = 0
            percentage_acquired = 100

        return level, xp_to_next_level, percentage_acquired

    def get_rank_exp(self, player_trophies):
        rank = 1
        trophies_required = 1000  # Initial trophies required for rank 1
        while rank < 6:
            if player_trophies >= trophies_required:
                player_trophies -= trophies_required
                rank += 1
                trophies_required += 500  # Increase trophies required by 500 for each rank
            else:
                break

        if rank < 6:
            trophies_to_next_rank = trophies_required - player_trophies
            percentage_acquired_rank = (1 - (trophies_to_next_rank / trophies_required)) * 100
        else:
            trophies_to_next_rank = 0
            percentage_acquired_rank = 100

        return rank, trophies_to_next_rank, percentage_acquired_rank
