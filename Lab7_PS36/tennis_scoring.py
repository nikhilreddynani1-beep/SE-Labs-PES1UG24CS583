def parse_score(text):
    a, b = text.split('-')
    return int(a), int(b)

def game_lead(text):
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    first, second = text.split('-')
    return points[first] - points[second]

def set_spread(games_csv):
    games = [int(g) for g in games_csv.split(',')]
    return max(games) - min(games)

def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)

if __name__ == "__main__":
    main()
