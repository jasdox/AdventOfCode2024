from itertools import product

f = open("input.txt", 'r')

data = []
line = f.readline()
# Reads in input and formats into array
while line != '':
    line = line.strip().split(":")
    line[0] = int(line[0])
    line[1] = line[1].strip().split(" ")
    for i in range(len(line[1])):
        line[1][i] = int(line[1][i])
    data.append(line)
    line = f.readline()

total = 0
operators = ['+', '*', '|']

# For every line generate a list of possible operators
for line in data:
    ops = list(product(operators, repeat=(len(line[1]) - 1)))

    # Go through possible operators until it matches the given value and if so, increase total
    for i in range(len(ops)):
        value = line[1][0]
        for j in range(len(ops[i])):
            match ops[i][j]:
                case '+':
                    value += line[1][j + 1]
                case '*':
                    value *= line[1][j + 1]
                case '|':
                    value = int(str(value) + str(line[1][j+1]))
        if value == line[0]:
            total += value
            break
print(total)


