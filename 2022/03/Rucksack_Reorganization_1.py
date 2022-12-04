
#                _                 _            __    _____          _             
#       /\      | |               | |          / _|  / ____|        | |            
#      /  \   __| |_   _____ _ __ | |_    ___ | |_  | |     ___   __| | ___        
#     / /\ \ / _` \ \ / / _ \ '_ \| __|  / _ \|  _| | |    / _ \ / _` |/ _ \       
#    / ____ \ (_| |\ V /  __/ | | | |_  | (_) | |   | |___| (_) | (_| |  __/       
#   /_/___ \_\__,_| \_/ \___|_| |_|\__|  \___/|_|    \_____\___/_\__,_|\___|  ___  
#   |  __ \                        | |               |___ \   |__ \ / _ \__ \|__ \ 
#   | |  | | ___  ___ ___ _ __ ___ | |__   ___ _ __    __) |     ) | | | | ) |  ) |
#   | |  | |/ _ \/ __/ _ \ '_ ` _ \| '_ \ / _ \ '__|  |__ <     / /| | | |/ /  / / 
#   | |__| |  __/ (_|  __/ | | | | | |_) |  __/ |     ___) |   / /_| |_| / /_ / /_ 
#   |_____/ \___|\___\___|_| |_| |_|_.__/ \___|_|    |____( ) |____|\___/____|____|
#                                                         |/                       
#     
# 🌲 https://patorjk.com/software/taag/#p=display&c=bash&f=Big&t=Advent%20of%20Code%0ADecember%203%2C%202022


# https://adventofcode.com/2022/day/3



alpha_check = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]


file1 = open('./input.txt', 'r')  # https://adventofcode.com/2022/day/3/input
Lines = file1.readlines()

total_value = 0

#
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
#

# 
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
#

def findMatch(string_one,string_two):
    global total_value
    for letter in string_one:

        if letter in string_two:
            # IT IS THE ONE
            total_value += (alpha_check.index(letter)+1)
            break

for line in Lines:
    corrent_line = line.strip()
    pocket_one = corrent_line[:int(len(corrent_line)//2)]

    pocket_two = corrent_line[int(len(corrent_line)//2):]

    findMatch(pocket_one,pocket_two)

    # print(pocket_one, pocket_two)
print("Total Value of all =>", total_value)

total = 0
for count in range(100):
    group = [Lines.pop(0), Lines.pop(0), Lines.pop(0)]
    for x in group[0]:
        if x in group[1] and x in group[2]:
            equal = True
            total += (alpha_check.index(x)+1)
            break

print("Part two:", total)