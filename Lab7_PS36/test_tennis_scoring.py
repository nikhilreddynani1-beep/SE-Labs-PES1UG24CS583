from hypothesis import given, settings, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread

POINT_NAMES = ["0", "15", "30", "40"]

# Score-like text: digits, separators and spaces in any order, so the fuzzer
# hits near-valid inputs such as "3-", "-2", "3--2", "6,,4" or " 4 , 6".
score_like = st.from_regex(r"\A[0-9 ,+-]{0,10}\Z")
any_input = st.text() | st.none() | score_like


# ---------------------------------------------------------------- parse_score
@settings(max_examples=500)
@given(any_input)
def test_parse_score_no_crash(s):
    try:
        result = parse_score(s)
    except Exception as e:
        assert False, f"parse_score crashed with: {e!r}"
    # Either rejected (None) or a pair of non-negative whole numbers.
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and all(isinstance(x, int) and x >= 0 for x in result)
    )


# Very long numbers: int() refuses strings of more than 4300 digits, and
# random text is very unlikely to contain one, so this is tested on its own.
@given(st.integers(min_value=4301, max_value=6000))
def test_parse_score_huge_number_no_crash(digits):
    try:
        result = parse_score("1" * digits + "-1")
    except Exception as e:
        assert False, f"parse_score crashed with: {e!r}"
    assert result is None or isinstance(result, tuple)


@given(st.integers(min_value=0, max_value=999),
       st.integers(min_value=0, max_value=999))
def test_parse_score_valid_round_trip(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


@given(st.integers(min_value=-999, max_value=-1),
       st.integers(min_value=0, max_value=999))
def test_parse_score_rejects_negative_points(a, b):
    assert parse_score(f"{a}-{b}") is None


# ------------------------------------------------------------------ game_lead
@settings(max_examples=500)
@given(any_input)
def test_game_lead_no_crash(s):
    try:
        result = game_lead(s)
    except Exception as e:
        assert False, f"game_lead crashed with: {e!r}"
    # Either rejected (None) or a lead between -3 and +3 points.
    assert result is None or (isinstance(result, int) and -3 <= result <= 3)


@given(st.sampled_from(POINT_NAMES), st.sampled_from(POINT_NAMES))
def test_game_lead_valid_scores(first, second):
    lead = game_lead(f"{first}-{second}")
    assert lead == POINT_NAMES.index(first) - POINT_NAMES.index(second)
    # Swapping the players flips the sign of the lead.
    assert game_lead(f"{second}-{first}") == -lead


# ----------------------------------------------------------------- set_spread
@settings(max_examples=500)
@given(any_input)
def test_set_spread_no_crash(s):
    try:
        result = set_spread(s)
    except Exception as e:
        assert False, f"set_spread crashed with: {e!r}"
    # Either rejected (None) or a non-negative spread.
    assert result is None or (isinstance(result, int) and result >= 0)


@given(st.lists(st.integers(min_value=0, max_value=7), min_size=1, max_size=5))
def test_set_spread_valid_sets(games):
    csv = ",".join(str(g) for g in games)
    assert set_spread(csv) == max(games) - min(games)
