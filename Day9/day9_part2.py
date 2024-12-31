# Returns the number of continuous spaces taken up by the id in the given disk
def count_id(disk, id, next_to_check):
    count = 0
    if next_to_check == -1:
        disk_to_check = disk
    else:
        disk_to_check = disk[:next_to_check + 1]
    for char in reversed(disk_to_check):
        if char == id:
            count += 1
        else:
            return count
    return count


# Returns the number of continuous open spaces starting at the given index
def count_next_open(disk, next_open):
    count = 0
    for i in range(next_open, len(disk)):
        if disk[i] == '.':
            count += 1
        else:
            return count
    return count


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
next_to_check = -1

# Iterate through the disk starting at the end
while len(disk) + next_to_check >= 0:
    progress = (abs(next_to_check) / len(disk)) * 100
    print("\r", f"{progress:.2f}" + "%", end='', flush=True)

    # If the next disk location being checked is not empty, find the next open spaces closest to the start of the disk
    # that can fit the current id and move all the continuous spaces in disk of the same id to those empty spaces
    if disk[next_to_check] != '.':
        id_count = count_id(disk, disk[next_to_check], next_to_check)
        open_count = count_next_open(disk, next_open)

        if next_open >= len(disk) + (next_to_check - id_count):
            next_to_check -= id_count

            next_open = disk.index('.')

        elif id_count <= open_count:
            for i in range(id_count):
                disk[next_open] = disk[next_to_check]
                disk.insert(next_to_check, '.')
                disk.pop(next_to_check)
                next_open += 1
                next_to_check -= 1
            next_open = disk.index('.')
        else:
            try:
                next_open = disk[next_open + open_count:].index('.') + (next_open + open_count)
            except ValueError:
                break

    else:
        next_to_check -= 1

check_sum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        check_sum += i * int(disk[i])

print()
print(check_sum)
