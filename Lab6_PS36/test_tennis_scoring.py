import pytest
from tennis_scoring import game_score, set_winner, match_status

#Example test cases:
def test_game_start():
    assert game_score(0, 0) == "0-0"

def test_set_undecided():
    assert set_winner(3, 2) is None

#Write the rest of the test cases so that the code is 90- 100% covered.
