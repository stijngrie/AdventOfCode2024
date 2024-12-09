import math

with open('Data/Day07Data.txt', 'r') as file:
    lines = list(map(str.strip, file))
    # Turn the rules into an array of arrays containing the 2 numbers as int
    testValues = list(map(lambda s: int(s.split(': ')[0]), lines))
    equations = list(map(lambda s: list(map(int, s.split(': ')[1].split(' '))), lines))


def part1():
    answer = 0
    for index in range(len(testValues)):
        # Set the wanted number as the Testvalue and pass the entire equation
        answer += testValues[index] if calculatePreviousNumber(testValues[index], equations[index]) else 0
    return str(answer)

def calculatePreviousNumber(wanted, numbers):
    # Check if the numbers array is only 1 number
    if len(numbers) == 1:
        # Check if the final number in the equation is the same as the wanted number, else the entire calculation is not possible
        return wanted == numbers[0]
    # Compare the last number in the equation to the wanted number
    # If the last equation number is in the table of the wanted number, multiplication is an option for this operator
    if wanted % numbers[len(numbers) - 1] == 0:
        # Pass the next wanted number as the wanted number divided by the last equation number, or pass the next wanted number as the wanted number minus the last equation number
        if calculatePreviousNumber(wanted=wanted / numbers[-1], numbers=numbers[:-1]): return True
    # If the last equation number is not in the tabke of the wanted number, just check for addition by passing the wanted number minus the last equation number
    else:
        if calculatePreviousNumber(wanted=wanted - numbers[-1], numbers=numbers[:-1]): return True
    return False
    
def part2():
    answer = 0
    for index in range(len(testValues)):
        # Set the wanted number as the Testvalue and pass the entire equation
        answer += testValues[index] if calculatePreviousNumber2(testValues[index], equations[index]) else 0
    return str(answer)

def calculatePreviousNumber2(wanted, numbers):
    # Check if the numbers array is only 1 number
    if len(numbers) == 1:
        # Check if the final number in the equation is the same as the wanted number, else the entire calculation is not possible
        return wanted == numbers[0]
    # Compare the last number in the equation to the wanted number
    # Pass the next wanted number as the wanted number divided by the last equation number, or pass the next wanted number as the wanted number minus the last equation number
    if wanted % numbers[-1] == 0 and calculatePreviousNumber2(wanted=wanted // numbers[-1], numbers=numbers[:-1]): return True 
    if wanted > numbers[-1] and calculatePreviousNumber2(wanted=wanted - numbers[-1], numbers=numbers[:-1]): return True
    if len(str(wanted)) > len(str(numbers[-1])) and str(wanted).endswith(str(numbers[-1])) and calculatePreviousNumber2(wanted=int(str(wanted)[:-len(str(numbers[-1]))]), numbers=numbers[:-1]): return True
    return False

print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())