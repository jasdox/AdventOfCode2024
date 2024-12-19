f = open("input.txt", 'r')

data = list(f.read())
# expected order of the mul command with i pointing to the next expected character
command_mul = ['m', 'u', 'l', '(', "n1", "n2"]
# expected order of the do/don't command with j pointing to the next expected character
command_do = ['d', 'o', 'n', "'", 't', '(', ')']
i = 0
j = 0

num1 = ''
num2 = ''
total_sum = 0
go = True

for char in data:
    next_expected_mul = command_mul[i]
    next_expected_do = command_do[j]

    # If the character is the next expected value for do/don't command, increase the do/don't index and if this is the
    # last index for the don't command, set do to false
    if char == next_expected_do:
        j += 1
        if next_expected_do == command_do[-1]:
            go = False
            j = 0
    # If we expect n for the don't command, but it is actually a '(', this is still possibly a do command, so increment
    # the index
    elif next_expected_do == 'n' and char == '(':
        j += 1
    # If we expect "'" for the don't command, but it is actually a ')', this is a do command, so set do to True and
    # rest the index
    elif next_expected_do == "'" and char == ')':
        go = True
        j = 0
    # If a character is not in line with the do/don't command, reset the index
    else:
        j = 0

    # Only check for mul commands if go is True
    if go:
        # If we expect the first number, concatenate all new digit characters into number 1 and move on when we see a ','
        if next_expected_mul == "n1":
            if char.isdigit():
                num1 += char
            elif char == ',':
                i += 1
            else:
                i = 0
                num1 = ''
                num2 = ''
        # If we expect the second number, concatenate all new digit characters into number 2 and add the product of the
        # numbers to the total sum when  we see a ')'
        elif next_expected_mul == "n2":
            if char.isdigit():
                num2 += char
            elif char == ')':
                i = 0
                total_sum += (int(num1) * int(num2))
                num1 = ''
                num2 = ''
            else:
                i = 0
                num1 = ''
                num2 = ''
        # move mul index along command while characters are as we expect
        elif char == next_expected_mul:
            i += 1
        # If a character is wrong reset the mul index
        else:
            i = 0

print(total_sum)

