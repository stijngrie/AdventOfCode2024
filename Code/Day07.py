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
    
def part2():
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
    # Pass the next wanted number as the wanted number divided by the last equation number, or pass the next wanted number as the wanted number minus the last equation number
    if wanted % numbers[-1] == 0 and calculatePreviousNumber(wanted // numbers[-1], numbers[:-1]): return True 
    if wanted > numbers[-1] and calculatePreviousNumber(wanted - numbers[-1], numbers[:-1]): return True
    if concat and len(str(wanted)) > len(str(numbers[-1])) and str(wanted).endswith(str(numbers[-1])) and calculatePreviousNumber(int(str(wanted)[:-len(str(numbers[-1]))]), numbers[:-1]): return True
    return False

concat = False
print("Part 1 answer: " + part1())
concat = True
print("Part 2 answer: " + part2())