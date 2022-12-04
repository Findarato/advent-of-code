#                _                 _            __    _____          _
#       /\      | |               | |          / _|  / ____|        | |
#      /  \   __| |_   _____ _ __ | |_    ___ | |_  | |     ___   __| | ___
#     / /\ \ / _` \ \ / / _ \ '_ \| __|  / _ \|  _| | |    / _ \ / _` |/ _ \
#    / ____ \ (_| |\ V /  __/ | | | |_  | (_) | |   | |___| (_) | (_| |  __/
#   /_/___ \_\__,_| \_/ \___|_| |_|\__|  \___/|_|    \_____\___/_\__,_|\___|  ___
#   |  __ \                        | |               | || |   |__ \ / _ \__ \|__ \
#   | |  | | ___  ___ ___ _ __ ___ | |__   ___ _ __  | || |_     ) | | | | ) |  ) |
#   | |  | |/ _ \/ __/ _ \ '_ ` _ \| '_ \ / _ \ '__| |__   _|   / /| | | |/ /  / /
#   | |__| |  __/ (_|  __/ | | | | | |_) |  __/ |       | |_   / /_| |_| / /_ / /_
#   |_____/ \___|\___\___|_| |_| |_|_.__/ \___|_|       |_( ) |____|\___/____|____|
#                                                         |/
#                                                           |/
# 🎄 https://patorjk.com/software/taag/#p=display&c=bash&f=Big&t=Advent%20of%20Code%0ADecember%204%2C%202022

# https://adventofcode.com/2022/day/4


input_file = open('./input.txt', 'r')
input_lines = input_file.readlines()

# https://adventofcode.com/2022/day/4/input


def generateRange(assignment):
    values = assignment.split('-')
    return set([n for n in range(int(values[0]),int(values[1])+1)])

total_inside = 0

total_outside = 0



for line in input_lines:
    assignments = line.strip().split(',')
    elf_one_assignments = generateRange(assignments[0])
    elf_two_assignments = generateRange(assignments[1])

    if elf_one_assignments.issubset(elf_two_assignments) or elf_two_assignments.issubset(elf_one_assignments):
        print("SUBSET")
        total_inside += 1

    if not elf_one_assignments.isdisjoint(elf_two_assignments):
        total_outside += 1


print("Part 1:", total_inside)
print("Part 2:", total_outside)