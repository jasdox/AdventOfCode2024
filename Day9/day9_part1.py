f = open("input.txt", 'r')

disk_map = f.read()
disk = []

# Constructs visual disk from map
for i in range(len(disk_map)):
    if i % 2 == 0:
        disk += ([str(int(i / 2))] * int(disk_map[i]))
    else:
        disk += (['.'] * int(disk_map[i]))

next_open = disk.index('.')

# Starting from the end of the disk, if there is a filled space, move it to the nearest unfilled space from the start
while True:
    if disk[-1] != '.':
        disk[next_open] = disk[-1]
        disk.pop(-1)
        try:
            next_open = disk.index('.')
        except ValueError:
            break
    else:
        disk.pop(-1)

check_sum = 0
for i in range(len(disk)):
    check_sum += i * int(disk[i])

print(check_sum)
