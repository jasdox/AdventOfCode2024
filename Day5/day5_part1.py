f = open("input.txt", 'r')

rules = []

# Read rules into rules array, splitting on '|' and converting to ints
line = f.readline().strip()
while len(line) != 0:
    rules.append(line.split('|'))
    rules[-1][0] = int(rules[-1][0])
    rules[-1][1] = int(rules[-1][1])
    line = f.readline().strip()

updates = []

# Read updates into update array, splitting on ',' and converting to ints
line = f.readline().strip()
while len(line) != 0:
    updates.append(line.split(','))
    updates[-1] = [int(num) for num in updates[-1]]
    line = f.readline().strip()

total = 0

for update in updates:
    correct = True

    # For every update, traverse the update backwards and see if any numbers are not allowed
    for i in reversed(range(len(update))):
        num = update[i]
        num_rules = list(filter(lambda r: r[0] == num, rules))

        # For every rule concerning the current number, if there is a number violating that rule earlier in the update,
        # this update is not correct
        for rule in num_rules:
            if rule[1] in update[0:i]:
                correct = False
                break
        if not correct:
            break

    # Sum all middle numbers of correct updates
    if correct:
        total += update[int(len(update) / 2)]

print(total)
