def choice(round_score, my_score, opponent_score):
    # TODO: return True if the player wants to roll again
    #       return False if the player wants to hold
    if player == 0:
        var = (input("You going again? Remember 99% of gamblers quit before their first big win. y/n:"))
        if var == "y":
            return True
        else:
            return False
    if player == 1:
        if scores[my_score] - scores[opponent_score] > 20:
            if score >= 23:
                return False
            else:
                return True
        elif scores[my_score] > scores[opponent_score] + 22:
            if score >= 22:
                return False
            else:
                return True
        elif scores[my_score] > scores[opponent_score]:
            if score >= 15:
                return False
            else:
                return True
        elif scores[opponent_score] + 18 > scores[my_score]:
            if score >= 10:
                return False
            else:
                return True
        elif scores[my_score] == scores[opponent_score]:
            if score >= 22:
                return False
            else:
                return True
        else:
            return False
