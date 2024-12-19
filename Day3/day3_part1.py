f = open("input.txt", 'r')

data = list(f.read())

# expected order of the command with i pointing to the next expected character
command = ['m', 'u', 'l', '(', "n1", "n2"]
i = 0

num1 = ''
num2 = ''
total_sum = 0

for char in data:
    next_expected = command[i]

    # If we expect the first number, concatenate all new digit characters into number 1 and move on when we see a ','
    if next_expected == "n1":
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
    elif next_expected == "n2":
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

    # move index along command while characters are as we expect
    elif char == next_expected:
        i += 1

    # If a character is wrong reset the index
    else:
        i = 0

print(total_sum)

