f = open("input.txt", 'r')
left = []
right =[]

# Reading input and separating the columns into two lists of ints
line = f.readline()
while line != "":
    line = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))
    line = f.readline()

total_score = 0

# For every number in the left list, add to total score that number times
# the number of times it appears in the right list
for num in left:
    total_score += (num * right.count(num))

print(total_score)