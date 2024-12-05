def check(numbers):
    # Get all the differences between the numbers in the sequence
    differences = []
    previousNumber = 0
    for number in numbers:
        differences.append(number - previousNumber)
        previousNumber = number
    differences = differences[1:]
    return all(1 <= difference <= 3 for difference in differences) or all(-1 >= difference >= -3 for difference in differences)

correctReports1 = 0
correctReports2 = 0
numbersList = []

with open('Data/Day02Data.txt', 'r') as file:
    for line in file:
         # Split the lines to get all the number in a list and then parse all to int
        numbersList.append(list(map(int, line.strip().split(' '))))

for numbers in numbersList:
    correctReports1 += 1 if check(numbers) else 0
    correctReports2 += 1 if any(check(numbers[:index] + numbers[index + 1:]) for index in range(len(numbers))) else 0

print("Part 1 answer: " + str(correctReports1))
print("Part 2 answer: " + str(correctReports2))