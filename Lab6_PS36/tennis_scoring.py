POINTS = ["0", "15", "30", "40"]


def game_score(a, b):
    if a < 0 or b < 0:
        raise ValueError("negative points")
    if a >= 3 and b >= 3:
        if a == b:
            return "deuce"
        if a - b >= 2:
            return "game A"
        if b - a >= 2:
            return "game B"
        if a > b:
            return "advantage A"
        return "advantage B"
    if a >= 4:
        return "game A"
    if b >= 4:
        return "game B"
    return POINTS[a] + "-" + POINTS[b]


def set_winner(a, b):
    if a >= 6 and a - b >= 2:
        return "A"
    if b >= 6 and b - a >= 2:
        return "B"
    if a == 7 and b == 6:
        return "A"
    if b == 7 and a == 6:
        return "B"
    return None


def match_status(sets_a, sets_b, best_of):
    needed = best_of // 2 + 1
    if sets_a == needed:
        return "A wins"
    if sets_b == needed:
        return "B wins"
    if sets_a == needed - 1 and sets_b == needed - 1:
        return "decider"
    return "in progress"
