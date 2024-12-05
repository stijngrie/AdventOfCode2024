def part1():
    with open('Data/Day03Data.txt', 'r') as file:
        input = ''.join(file)
        # Get all the instances where the mul( is typed correctly
        instances = input.split('mul(')
        answer = 0
        # Loop over all the instances
        for instance in instances:
            # Check if the mul statement closes correctly and get the 2 numbers in the statement
            possibleNumbers = instance.split(')')[0].split(',')
            # Check if there are 2 entries and if both are numbers
            correctMul = len(possibleNumbers) == 2 and all(number.isnumeric() for number in possibleNumbers)
            if correctMul:
                answer += int(possibleNumbers[0]) * int(possibleNumbers[1])
        return str(answer)
    
def part2():
    with open('Data/Day03Data.txt', 'r') as file:
        input = ''.join(file)
        # Get only the substrings from after a do() statement 
        tempSplits = input.split('do()')
        doSplits = []
        # Check all of these for don't() statements and remove all text after that
        for split in tempSplits:
            doSplits.append(split.split("don't()")[0])
        doInput = ''.join(doSplits)
        # Do the same as in part one but with only the enabled parts
        instances = doInput.split('mul(')
        answer = 0
        # Loop over all the instances
        for instance in instances:
            # Check if the mul statement closes correctly and get the 2 numbers in the statement
            possibleNumbers = instance.split(')')[0].split(',')
            # Check if there are 2 entries and if both are numbers
            correctMul = len(possibleNumbers) == 2 and all(number.isnumeric() for number in possibleNumbers)
            if correctMul:
                answer += int(possibleNumbers[0]) * int(possibleNumbers[1])
        return str(answer)

print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())