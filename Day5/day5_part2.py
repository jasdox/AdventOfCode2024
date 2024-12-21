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
    fixed = True
    solved = False

    # Repeat this solving section until the update does not need to be fixed anymore
    while not solved:
        solved = True

        # For every update, traverse the update backwards and see if any numbers are not allowed
        for i in reversed(range(len(update))):
            num = update[i]
            num_rules = list(filter(lambda r: r[0] == num, rules))

            # For every rule concerning the current number, if there is a number violating that rule earlier in the update,
            # swap the current number and the violating number in the update
            for rule in num_rules:
                if rule[1] in update[0:i]:
                    solved = False
                    fixed = False
                    index = update.index(rule[1])
                    update[index] = update[i]
                    update[i] = rule[1]
                    i -= 1

    # Sum all middle numbers of fixed updates
    if not fixed:
        total += update[int(len(update) / 2)]

print(total)
