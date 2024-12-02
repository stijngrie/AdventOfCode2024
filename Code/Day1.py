

def part1():
    leftNumbers = []
    rightNumbers = []
    difference = 0

    with open('Data/Day1Data.txt', 'r') as file:
        for line in file:
            numbers = line.strip().split('   ')
            leftNumbers.append(int(numbers[0]))
            rightNumbers.append(int(numbers[1]))

    leftNumbers.sort()
    rightNumbers.sort()

    for x in range(len(leftNumbers)):
        difference += abs(leftNumbers[x] - rightNumbers[x])
    return str(difference)

def part2():
    leftNumbers = []
    rightNumbers = []
    similarity = 0
    numberAmounts = dict()

    with open('Data/Day1Data.txt', 'r') as file:
        for line in file:
            numbers = line.strip().split('   ')
            leftNumbers.append(int(numbers[0]))
            rightNumbers.append(int(numbers[1]))

    for number in rightNumbers:
        if number in numberAmounts:
            numberAmounts[number] += 1
        else:
            numberAmounts[number] = 1

    for number in leftNumbers:
        if number in numberAmounts:
            similarity +=  number * numberAmounts[number]
    
    return str(similarity)

print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())