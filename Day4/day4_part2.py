# Returns true if this letter is the center of an x-mas X
def scan(row, col, words):
    if words[row][col] == 'A':
        word1 = [words[row-1][col-1], words[row+1][col+1]]
        word2 = [words[row+1][col-1], words[row-1][col+1]]

        word1b = (word1[0] == 'M' and word1[1] == 'S') or (word1[0] == 'S' and word1[1] == 'M')
        word2b = (word2[0] == 'M' and word2[1] == 'S') or (word2[0] == 'S' and word2[1] == 'M')

        if word1b and word2b:
            return True


f = open("input.txt", 'r')

words = []

# Setup words array to have empty border
line = f.readline()
while line != '':
    line = list((line.strip()))
    line.insert(0, '')
    line.append('')
    words.append(line)
    line = f.readline()

words.insert(0, [''] * (len(words[0])))
words.append([''] * (len(words[0])))

xmas_count = 0

# Iterate through every letter in the input and check if it is the center of an x-mas X
for row in range(1, len(words) - 1):
    for col in range(1, len(words[0]) - 1):
        letter = words[row][col]
        if scan(row, col, words):
            xmas_count += 1

print(xmas_count)
