from random import randint

TARGET_GUESSES = []
for x in range(4):
    TARGET_GUESSES.append(x)

TARGET_COORDINATES = []
for x in range(4):
    TARGET_COORDINATES.append(x)

def show_coordinates(map):
    print("A B C D")
    line_number = 1
    for line in map:
        print("%d|%s|" % line_number, "|".join(line))
        line_number +=1


show_coordinates(map)
