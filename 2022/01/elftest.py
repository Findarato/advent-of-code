#                _                 _            __    _____          _
#       /\      | |               | |          / _|  / ____|        | |
#      /  \   __| |_   _____ _ __ | |_    ___ | |_  | |     ___   __| | ___
#     / /\ \ / _` \ \ / / _ \ '_ \| __|  / _ \|  _| | |    / _ \ / _` |/ _ \
#    / ____ \ (_| |\ V /  __/ | | | |_  | (_) | |   | |___| (_) | (_| |  __/
#   /_/    \_\__,_| \_/ \___|_| |_|\__|  \___/|_|    \_____\___/ \__,_|\___|
#    _____                          _                 __     ___   ___ ___  ___
#   |  __ \                        | |               /_ |   |__ \ / _ \__ \|__ \
#   | |  | | ___  ___ ___ _ __ ___ | |__   ___ _ __   | |      ) | | | | ) |  ) |
#   | |  | |/ _ \/ __/ _ \ '_ ` _ \| '_ \ / _ \ '__|  | |     / /| | | |/ /  / /
#   | |__| |  __/ (_|  __/ | | | | | |_) |  __/ |     | |_   / /_| |_| / /_ / /_
#   |_____/ \___|\___\___|_| |_| |_|_.__/ \___|_|     |_( ) |____|\___/____|____|
#                                                       |/
# https://patorjk.com/software/taag/#p=display&c=bash&f=Big&t=Advent%20of%20Code%0ADecember%201%2C%202022

#
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
#


file1 = open('./input.txt', 'r')
Lines = file1.readlines()


elves = []

current_elf = 0 # To keep track of the current elf


for line in Lines:
    current_line = line.strip()
    # current_line = line
    if line == "" or line is None  or len(current_line) == 0: # We have a new elf
        elves.append(current_elf)
        current_elf = 0 # Reset the elf
    else:
        # print(int(current_line))
        current_elf += int(current_line)

elves.sort(reverse=True) # Lets get them in order

# print(elf_number, elves)

print("Highest Calorie elf:", elves[0])

### That's the right answer! You are one gold star closer to collecting enough star fruit. [Continue to Part Two]

print("Top 3 Calorie Elves", elves[0],elves[1],elves[2])
print("Total Calories in top 3", elves[0]+elves[1]+elves[2])

### That's the right answer! You are one gold star closer to collecting enough star fruit.
# You have completed Day 1! You can [Shareon Twitter Mastodon] this victory or [Return to Your Advent Calendar].
