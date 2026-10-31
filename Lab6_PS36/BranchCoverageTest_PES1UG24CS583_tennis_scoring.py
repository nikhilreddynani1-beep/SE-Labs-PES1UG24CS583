"""Lab 6 - branch coverage tests for tennis_scoring.py.

Goal: take every decision (if) in tennis_scoring.py both ways (True and
False), and exercise each part of the compound conditions and the
boundary values around them.

Run:
    coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_tennis_scoring.py
    coverage report -m
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score
# if a < 0 or b < 0  ->  True through either operand, and False
@pytest.mark.parametrize("a, b", [(-1, 0), (0, -1), (-2, -3)])
def test_game_negative_points_rejected(a, b):
    with pytest.raises(ValueError):
        game_score(a, b)


# if a >= 3 and b >= 3  ->  False (normal scoring, either side below 3)
@pytest.mark.parametrize("a, b, expected", [
    (0, 0, "0-0"),
    (1, 0, "15-0"),
    (0, 2, "0-30"),
    (2, 2, "30-30"),
    (3, 2, "40-30"),   # a >= 3 True,  b >= 3 False
    (2, 3, "30-40"),   # a >= 3 False, b >= 3 True
    (3, 0, "40-0"),
])
def test_game_normal_scoring(a, b, expected):
    assert game_score(a, b) == expected


# if a >= 3 and b >= 3  ->  True: deuce / advantage / game, both players
@pytest.mark.parametrize("a, b, expected", [
    (3, 3, "deuce"),
    (4, 4, "deuce"),
    (10, 10, "deuce"),         # long deuce
    (4, 3, "advantage A"),
    (3, 4, "advantage B"),
    (11, 10, "advantage A"),
    (10, 11, "advantage B"),
    (5, 3, "game A"),          # a - b >= 2 True
    (3, 5, "game B"),          # b - a >= 2 True
    (12, 10, "game A"),
    (10, 12, "game B"),
])
def test_game_after_both_reach_40(a, b, expected):
    assert game_score(a, b) == expected


# if a >= 4 / if b >= 4  ->  game won before deuce is possible
@pytest.mark.parametrize("a, b, expected", [
    (4, 0, "game A"),
    (4, 2, "game A"),
    (0, 4, "game B"),
    (2, 4, "game B"),
])
def test_game_won_without_deuce(a, b, expected):
    assert game_score(a, b) == expected


# ---------------------------------------------------------------- set_winner
@pytest.mark.parametrize("a, b, expected", [
    (6, 0, "A"),
    (6, 4, "A"),       # a >= 6 True, a - b >= 2 True
    (7, 5, "A"),
    (0, 6, "B"),
    (4, 6, "B"),       # b >= 6 True, b - a >= 2 True
    (5, 7, "B"),
    (7, 6, "A"),       # tiebreak won by A
    (6, 7, "B"),       # tiebreak won by B
])
def test_set_decided(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize("a, b", [
    (0, 0),
    (3, 2),
    (5, 4),            # a >= 6 False
    (6, 5),            # a >= 6 True, a - b >= 2 False
    (5, 6),            # b >= 6 True, b - a >= 2 False
    (6, 6),            # tiebreak still to be played
    (7, 7),            # a == 7 True, b == 6 False / b == 7 True, a == 6 False
])
def test_set_undecided(a, b):
    assert set_winner(a, b) is None


# -------------------------------------------------------------- match_status
@pytest.mark.parametrize("sets_a, sets_b, best_of, expected", [
    # best of 3: 2 sets needed
    (2, 0, 3, "A wins"),
    (2, 1, 3, "A wins"),
    (0, 2, 3, "B wins"),
    (1, 2, 3, "B wins"),
    (1, 1, 3, "decider"),
    (0, 0, 3, "in progress"),
    (1, 0, 3, "in progress"),     # sets_a == needed - 1 True, sets_b False
    (0, 1, 3, "in progress"),     # sets_a == needed - 1 False
    # best of 5: 3 sets needed
    (3, 0, 5, "A wins"),
    (3, 2, 5, "A wins"),
    (1, 3, 5, "B wins"),
    (2, 2, 5, "decider"),
    (2, 1, 5, "in progress"),
    (0, 0, 5, "in progress"),
    # best of 1: 1 set needed, so 0-0 is already the decider
    (1, 0, 1, "A wins"),
    (0, 1, 1, "B wins"),
    (0, 0, 1, "decider"),
])
def test_match_status(sets_a, sets_b, best_of, expected):
    assert match_status(sets_a, sets_b, best_of) == expected
