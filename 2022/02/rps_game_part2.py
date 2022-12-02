
#                _                 _            __    _____          _
#       /\      | |               | |          / _|  / ____|        | |
#      /  \   __| |_   _____ _ __ | |_    ___ | |_  | |     ___   __| | ___
#     / /\ \ / _` \ \ / / _ \ '_ \| __|  / _ \|  _| | |    / _ \ / _` |/ _ \
#    / ____ \ (_| |\ V /  __/ | | | |_  | (_) | |   | |___| (_) | (_| |  __/
#   /_/___ \_\__,_| \_/ \___|_| |_|\__|  \___/|_|    \_____\___/_\__,_|\___|  ___
#   |  __ \                        | |               |__ \    |__ \ / _ \__ \|__ \
#   | |  | | ___  ___ ___ _ __ ___ | |__   ___ _ __     ) |      ) | | | | ) |  ) |
#   | |  | |/ _ \/ __/ _ \ '_ ` _ \| '_ \ / _ \ '__|   / /      / /| | | |/ /  / /
#   | |__| |  __/ (_|  __/ | | | | | |_) |  __/ |     / /_ _   / /_| |_| / /_ / /_
#   |_____/ \___|\___\___|_| |_| |_|_.__/ \___|_|    |____( ) |____|\___/____|____|
#                                                         |/
#                                                      |/
# 🌲 https://patorjk.com/software/taag/#p=display&c=bash&f=Big&t=Advent%20of%20Code%0ADecember%202%2C%202022


# A => Rock    => 1 Point
# B => Paper   => 2 Points
# C => Sissors => 3 Points

# X => lose
# Y => Draw
# Z => Win

# Loss => 0
# Tie  => 3
# Win  => 6


file1 = open('./input.txt', 'r')  # https://adventofcode.com/2022/day/2/input
Lines = file1.readlines()


current_score = 0

opponent_values = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

outcome = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

def score_me(play, adjusted_score):

    if play == "Rock":
        adjusted_score += 1
    elif play == "Paper":
        adjusted_score += 2
    else:
        adjusted_score += 3
    return adjusted_score


def did_i_win(opponent, outcome):

    global current_score

    # Quick Tie test
    if outcome == "Lose":
        if opponent == "Rock":
            # This one I know the result
            current_score = score_me("Scissors", current_score)
            print("🪨","✂")
        elif opponent == "Paper":
            # This one I know the result
            current_score = score_me("Rock", current_score)
            print("📰","🪨")
        elif opponent == "Scissors":
            # This one I know the result
            print("✂","📰")
            current_score = score_me("Paper", current_score)
        return "Lose"

    if outcome == "Win":
        current_score += 6
        # current_score = score_me(opponent, current_score)  # This one I know the result
        if opponent == "Rock":
            # This one I know the result
            current_score = score_me("Paper", current_score)
            print("🪨","📰")
        elif opponent == "Paper":
            # This one I know the result
            current_score = score_me("Scissors", current_score)
            print("📰","✂")
        elif opponent == "Scissors":
            # This one I know the result
            current_score = score_me("Rock", current_score)
            print("✂","🪨")

        return "Win"


    current_score += 3
    # This one I know the result
    current_score = score_me(opponent, current_score)
    return "Draw"

for line in Lines:
    current_match = line.strip()
    match_results = current_match.split()

    results = did_i_win(
        opponent_values[match_results[0]], outcome[match_results[1]])
    print(results, current_score)


# That's the right answer! You are one gold star closer to collecting enough star fruit.