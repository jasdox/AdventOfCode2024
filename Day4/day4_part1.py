# Returns the number of "xmas" words that originate from the given row, col position. cur_letter refers to which letter
# in the word we are currently looking for. v and h represent the direction that the word is going once we have found
# at lest two letters in a row. cur_letter, v, and h are 0 when calling this function from outside itself.
def scan(row, col, words, cur_letter, v, h):
    word = ['X', 'M', 'A', 'S']

    if words[row][col] == word[cur_letter]:
        cur_letter += 1
    else:
        return 0

    total_words = 0

    # For the first time, search surrounding letters and if one is the next letter we need, call this function recursively, informing it of
    # the direction the word should be reading
    if v == 0 and h == 0:
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if words[i][j] == word[cur_letter]:
                    if cur_letter == len(word) - 1:
                        return 1 + total_words
                    else:

                        total_words += scan(i, j, words, cur_letter, i - row, j - col)

    # If we are continuing searching in a particular word, just check if the next letter is in the direction the word is
    # already oriented
    else:
        if words[row + v][col + h] == word[cur_letter]:
            if cur_letter == len(word) - 1:
                return 1 + total_words
            else:
                total_words += scan(row + v, col + h, words, cur_letter, v, h)

    return total_words


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

# Iterate through every letter in the input and check if/how many xmas words originates from there
for row in range(1, len(words) - 1):
    for col in range(1, len(words[0]) - 1):
        letter = words[row][col]
        xmas_count += scan(row, col, words, 0, 0, 0)

print(xmas_count)
