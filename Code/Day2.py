

def part1():
    correctReports = 0
    with open('Data/Day2Data.txt', 'r') as file:
        for line in file:
            # Split the lines to get all the number in a list and then parse all to int
            numbers = list(map(int, line.strip().split(' ')))
            # Set the initial number
            previousNumber = numbers[0]
            # Check if the numbers are increasing or not
            increasing = numbers[1] > numbers[0]
            correct = True
            for index in range(len(numbers)):   
                # Skip the first number
                if index == 0:
                    break
                # Check if the next number is increasing or decreasing
                diff = numbers[index] - previousNumber
                if (increasing and (diff < 1 or diff > 3)):
                    correct = False
                if (not increasing and (diff > -1 or diff < -3)):
                    correct = False
            # If the sequence was correct, add to var
            if correct:
                correctReports += 1  
    return str(correctReports)


def part2():
    return ''

print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())