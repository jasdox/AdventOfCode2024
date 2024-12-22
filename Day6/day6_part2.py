import copy

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def is_loop(guard_map, start_pos):
    k = 0
    cur_direction = UP
    cur_pos = copy.deepcopy(start_pos)

    # If this loop has been running for an arbitrarily large number of iterations, we have a loop
    while True:
        if k == 10000:
            return True

        # If the next space in the current direction is empty, break out of loop, if it is an obstacle, change direction
        # 90 degrees to the right, otherwise change the current position to one forward in the current direction
        match cur_direction:
            case 0:
                if guard_map[cur_pos[0] - 1][cur_pos[1]] == '':
                    break
                elif guard_map[cur_pos[0] - 1][cur_pos[1]] != '#':
                    cur_pos[0] = cur_pos[0] - 1
                else:
                    cur_direction += 1
            case 1:
                if guard_map[cur_pos[0]][cur_pos[1] + 1] == '':
                    break
                elif guard_map[cur_pos[0]][cur_pos[1] + 1] != '#':
                    cur_pos[1] = cur_pos[1] + 1
                else:
                    cur_direction += 1
            case 2:
                if guard_map[cur_pos[0] + 1][cur_pos[1]] == '':
                    break
                elif guard_map[cur_pos[0] + 1][cur_pos[1]] != '#':
                    cur_pos[0] = cur_pos[0] + 1
                else:
                    cur_direction += 1
            case 3:
                if guard_map[cur_pos[0]][cur_pos[1] - 1] == '':
                    break
                elif guard_map[cur_pos[0]][cur_pos[1] - 1] != '#':
                    cur_pos[1] = cur_pos[1] - 1
                else:
                    cur_direction = UP
        k += 1
    return False


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

start_pos = [-1, -1]

# Find the starting position
for i in range(1, len(guard_map) - 1):
    for j in range(1, len(guard_map[0]) - 1):
        if guard_map[i][j] == '^':
            start_pos = [i, j]
            break

total = 0
# Place a new obstacle in every open position in the map, and check if this map creates a loop
for i in range(1, len(guard_map) - 1):
    for j in range(1, len(guard_map[0]) - 1):
        if guard_map[i][j] != '.':
            continue
        new_guard_map = copy.deepcopy(guard_map)
        new_guard_map[i][j] = '#'
        if is_loop(new_guard_map, start_pos):
            total += 1

        progress = (i * len(guard_map[0]) + j) / ((len(guard_map) - 1) * (len(guard_map[0]) - 1)) * 100
        print("\r", f"{progress:.2f}" + "%", end='', flush=True)
print()
print(total)
