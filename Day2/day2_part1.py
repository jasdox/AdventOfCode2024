INCREASING = 1
DECREASING = 0

f = open("input.txt", 'r')

total_safe = 0

line = f.readline()
while line != "":
    safe = True
    split_line = line.split()

    # Set order to increasing if the first two numbers are going up or decreasing if the first two numbers are going
    # down otherwise, move past this line
    if int(split_line[1]) - int(split_line[0]) > 0:
        order = INCREASING
    elif int(split_line[1]) - int(split_line[0]) < 0:
        order = DECREASING
    else:
        line = f.readline()
        continue

    # If the order is increasing, check each pair of numbers and if it does not increase by 1, 2, or 3, set safe to
    # false for this line
    if order == INCREASING:
        for i in range(len(split_line) - 1):
            diff = int(split_line[i + 1]) - int(split_line[i])
            if diff < 1 or diff > 3:
                safe = False
                break

    # If the order is decreasing, check each pair of numbers and if it does not decrease by 1, 2, or 3, set safe to
    # false for this line
    if order == DECREASING:
        for i in range(len(split_line) - 1):
            diff = int(split_line[i]) - int(split_line[i + 1])
            if diff < 1 or diff > 3:
                safe = False
                break

    # Update sum if the line was safe
    if safe:
        total_safe += 1

    line = f.readline()

print(total_safe)
