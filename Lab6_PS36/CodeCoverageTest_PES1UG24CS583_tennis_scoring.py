"""Lab 6 - code (line) coverage tests for tennis_scoring.py.

Goal: execute at least 90% of the statements in tennis_scoring.py.
One test per typical outcome of each function.

Run:
    coverage run -m pytest CodeCoverageTest_PES1UG24CS583_tennis_scoring.py
    coverage report -m
"""
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------------------------------------------------------- game_score
def test_game_start():
    assert game_score(0, 0) == "0-0"


def test_game_normal_points():
    assert game_score(1, 0) == "15-0"
    assert game_score(3, 2) == "40-30"


def test_game_negative_points_rejected():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_game_won_by_a_after_deuce():
    assert game_score(5, 3) == "game A"


def test_game_won_by_b_after_deuce():
    assert game_score(3, 5) == "game B"


def test_game_won_by_a_to_love():
    assert game_score(4, 0) == "game A"


def test_game_won_by_b_without_deuce():
    assert game_score(1, 4) == "game B"


# ---------------------------------------------------------------- set_winner
def test_set_undecided():
    assert set_winner(3, 2) is None


def test_set_won_by_a():
    assert set_winner(6, 4) == "A"


def test_set_won_by_b():
    assert set_winner(3, 6) == "B"


def test_set_tiebreak_won_by_a():
    assert set_winner(7, 6) == "A"


# -------------------------------------------------------------- match_status
def test_match_a_wins_best_of_3():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins_best_of_3():
    assert match_status(1, 2, 3) == "B wins"


def test_match_decider_best_of_3():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"
    assert match_status(2, 1, 5) == "in progress"
