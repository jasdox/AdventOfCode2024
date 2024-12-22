UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

f = open("input.txt", 'r')

guard_map = []

# Read input into matrix with empty borders
line = f.readline()
while line != '':
    line = list((line.strip()))
    line.insert(0, '')
    line.append('')
    guard_map.append(line)
    line = f.readline()

guard_map.insert(0, [''] * (len(guard_map[0])))
guard_map.append([''] * (len(guard_map[0])))

cur_pos = [-1, -1]
cur_direction = UP

# Find the starting position and mark it with 'X'
for i in range(1, len(guard_map) - 1):
    for j in range(1, len(guard_map[0]) - 1):
        if guard_map[i][j] == '^':
            cur_pos = [i, j]
            guard_map[i][j] = 'X'
            break


while True:
    # If the next space in the current direction is empty, break out of loop, if it is an obstacle, change direction
    # 90 degrees to the right, otherwise change the current position to one forward in the current direction and mark
    # the spot with an 'X'
    match cur_direction:
        case 0:
            if guard_map[cur_pos[0] - 1][cur_pos[1]] == '':
                break
            elif guard_map[cur_pos[0] - 1][cur_pos[1]] != '#':
                cur_pos[0] = cur_pos[0] - 1
                guard_map[cur_pos[0]][cur_pos[1]] = 'X'
            else:
                cur_direction += 1
        case 1:
            if guard_map[cur_pos[0]][cur_pos[1] + 1] == '':
                break
            elif guard_map[cur_pos[0]][cur_pos[1] + 1] != '#':
                cur_pos[1] = cur_pos[1] + 1
                guard_map[cur_pos[0]][cur_pos[1]] = 'X'
            else:
                cur_direction += 1
        case 2:
            if guard_map[cur_pos[0] + 1][cur_pos[1]] == '':
                break
            elif guard_map[cur_pos[0] + 1][cur_pos[1]] != '#':
                cur_pos[0] = cur_pos[0] + 1
                guard_map[cur_pos[0]][cur_pos[1]] = 'X'
            else:
                cur_direction += 1
        case 3:
            if guard_map[cur_pos[0]][cur_pos[1] - 1] == '':
                break
            elif guard_map[cur_pos[0]][cur_pos[1] - 1] != '#':
                cur_pos[1] = cur_pos[1] - 1
                guard_map[cur_pos[0]][cur_pos[1]] = 'X'
            else:
                cur_direction = UP

# Count all 'X's
total = 0
for line in guard_map:
    total += line.count('X')

print(total)
