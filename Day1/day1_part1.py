f = open("input.txt", 'r')
left = []
right = []

# Reading input and separating the columns into two lists of ints
line = f.readline()
while line != "":
    line = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))
    line = f.readline()

total_distance = 0

# Taking the min numbers from both lists, popping them out, and adding their difference to total distance until
# no numbers are remaining
for i in range(len(right)):
    minL = min(left)
    minR = min(right)
    left.pop(left.index(minL))
    right.pop(right.index(minR))

    total_distance += abs(minL - minR)

print(total_distance)

f.close()
