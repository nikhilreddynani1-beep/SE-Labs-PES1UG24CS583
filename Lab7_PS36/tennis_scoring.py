"""Tennis scoring helpers, hardened against invalid input.

Every function returns None for input it cannot interpret, instead of
crashing, so callers (and main) can report the problem to the user.
"""
import re

POINTS = {'0': 0, '15': 1, '30': 2, '40': 3}

# A count is 1-4 plain ASCII digits. This rejects signs, decimals, empty
# parts, Unicode digits such as '²' or '٣', and numbers too long for int()
# (Python refuses to convert strings of more than 4300 digits).
COUNT_PATTERN = re.compile(r"[0-9]{1,4}")


def _to_count(part):
    """Return part as a non-negative int, or None if it is not a valid count."""
    part = part.strip()
    if not COUNT_PATTERN.fullmatch(part):
        return None
    return int(part)


def _split_pair(text):
    """Split 'X-Y' into two stripped parts, or return None."""
    if not isinstance(text, str):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    return parts[0].strip(), parts[1].strip()


def parse_score(text):
    """Parse points won as 'A-B' into (A, B); None if invalid."""
    pair = _split_pair(text)
    if pair is None:
        return None
    a, b = _to_count(pair[0]), _to_count(pair[1])
    if a is None or b is None:
        return None
    return a, b


def game_lead(text):
    """Lead of the first player in a game score such as '40-30'; None if invalid."""
    pair = _split_pair(text)
    if pair is None:
        return None
    first, second = pair
    if first not in POINTS or second not in POINTS:
        return None
    return POINTS[first] - POINTS[second]


def set_spread(games_csv):
    """Difference between the most and fewest games in a CSV such as '6,4,7'; None if invalid."""
    if not isinstance(games_csv, str):
        return None
    games = [_to_count(g) for g in games_csv.split(',')]
    if any(g is None for g in games):
        return None
    return max(games) - min(games)


def _ask(prompt):
    """Read one line of input; None if input has ended (e.g. Ctrl+Z / Ctrl+D)."""
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    print("==== Running parse_score ====")
    user_input = _ask("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    if result is None:
        print("Invalid input: expected two whole numbers like 3-2.")
    else:
        print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = _ask("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    if result is None:
        print("Invalid input: expected two of 0, 15, 30, 40 like 40-30.")
    else:
        print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = _ask("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    if result is None:
        print("Invalid input: expected whole numbers separated by commas like 6,4,7.")
    else:
        print("Spread:", result)


if __name__ == "__main__":
    main()
