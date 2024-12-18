import copy

# Returns true if this line is decreasing by 1, 2, or 3 every number
def check_decreasing_line(line):
    i = 0
    while i is not len(line) - 1:
        diff = int(line[i]) - int(line[i + 1])
        if diff < 1 or diff > 3:
            return False
        i += 1
    return True


# Returns true if this line is increasing by 1, 2, or 3 every number
def check_increasing_line(line):
    i = 0
    while i is not len(line) - 1:
        diff = int(line[i + 1]) - int(line[i])
        if diff < 1 or diff > 3:
            return False
        i += 1
    return True


f = open("input.txt", 'r')

total_safe = 0

line = f.readline()
while line != "":
    unsafe_levels = 0
    split_line = line.split()

    # Check if the line is valid either increasing or decreasing, updating total sum
    if check_increasing_line(split_line) or check_decreasing_line(split_line):
        total_safe += 1
    # If the line is not valid, test if it would be valid after removing each index, updating total sum
    else:
        for i in range(len(split_line)):
            line_copy = copy.deepcopy(split_line)
            del line_copy[i]
            if check_increasing_line(line_copy) or check_decreasing_line(line_copy):
                total_safe += 1
                break

    line = f.readline()

print(total_safe)
