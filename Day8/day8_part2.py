from fractions import  Fraction

f = open("input.txt", 'r')

puzzle_map = []
antennas = []
frequencies = set()
locations = set()

line = f.readline()
hLen = len(line) - 1
i = 0

# Read map from file into matrix and add all antenna positions to a list and add all unique frequencies to a set
while line != '':
    line = list((line.strip()))
    for j in range(len(line)):
        if line[j] != '.':
            antennas.append([i, j, line[j]])
            frequencies.add(line[j])
    puzzle_map.append(line)
    line = f.readline()
    i += 1
vLen = i

# For every unique frequency, filter all antenna positions belonging to that frequency
for freq in frequencies:
    ant = list(filter(lambda a: a[2] == freq, antennas))
    if len(ant) <= 1:
        continue

# For every pair of antennas of this frequency, add a location to the list that is in the same
# direction as the second antenna from the first and repeat until we've gone off the map
    for i in range(len(ant)):
        locations.add((ant[i][0], ant[i][1]))
        for j in range(len(ant)):
            if i == j:
                continue
            v = ant[j][0] - ant[i][0]
            if v > 0:
                v_sign = 1
            else:
                v_sign = -1

            h = ant[j][1] - ant[i][1]
            if h > 0:
                h_sign = 1
            else:
                h_sign = -1

            # Reduces the fraction if possible
            fraction = Fraction(v, h)
            v = abs(fraction.numerator) * v_sign
            h = abs(fraction.denominator) * h_sign

            k = 1
            while True:
                pos = (ant[j][0] + (v * k), ant[j][1] + (h * k))
                if 0 <= pos[0] < vLen and 0 <= pos[1] < hLen:
                    locations.add(pos)
                    puzzle_map[pos[0]][pos[1]] = '#'
                else:
                    break
                k += 1

for line in puzzle_map:
    for char in line:
        print(char, end='')
    print()

print(len(locations))
