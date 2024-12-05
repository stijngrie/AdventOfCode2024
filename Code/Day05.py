import math

with open('Data/Day05Data.txt', 'r') as file:
    lines = list(map(str.strip, file))
    # Find where the empty line is to split between rules and updates
    splitIndex = lines.index('')
    # Turn the rules into an array of arrays containing the 2 numbers as int
    rules = list(map(lambda s: list(map(int, s.split('|'))), lines[:splitIndex]))
    # Do the same for the updates
    updates = list(map(lambda s: list(map(int, s.split(','))),lines[splitIndex + 1:]))

def part1():
    answer = 0
    # Loop over all the updates
    for update in updates:
        # Check if all rules apply on this update by checking if the first number of a rule does not appear before the second number making the rule invalid
        correct = not any(rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]) for rule in rules)
        # Get the middle number of the updates array to add to answer
        answer += update[math.floor(len(update)/2)] if correct else 0
    
    return str(answer)
    
def part2():
    answer = 0
    sortingUpdates = []
    correctUpdates = []
    # Loop over all the updates
    for update in updates:
        # Check if valid again but add to new array when invalid
        correct = not any(rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]) for rule in rules)
        sortingUpdates.append(update) if not correct else 0
        
    # Loop over the updates continuously until all are valid
    sorted = False
    while not sorted:
        # Initially set sorted to true and create a copy list
        newSortingUpdates = []
        sorted = True
        for update in sortingUpdates:
            # Check if valid again but add to new array when invalid
            correct = not any(rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]) for rule in rules)
            if not correct:
                newUpdate = update[:]
                # Set sorted to false
                sorted = False
                # Loop over rules to reindex wrong rules
                for rule in rules:    
                    # Check if rule is false
                    if rule[0] in newUpdate and rule[1] in newUpdate and newUpdate.index(rule[0]) > newUpdate.index(rule[1]):
                        rule1Index = newUpdate.index(rule[0])
                        rule2Index = newUpdate.index(rule[1])
                        secondNum = newUpdate.pop(rule1Index)
                        newUpdate.insert(rule2Index, secondNum)
                # Add the newUpdate to the new array for the next loop
                newSortingUpdates.append(newUpdate)
            # If correct, add to correct array
            else:
                correctUpdates.append(update)
        # Set sortingupdates to the newsortingupdate to refresh the loop
        sortingUpdates = newSortingUpdates[:]
       
    # When the loop ends, do the math for the middle numbers
    for update in correctUpdates:
        answer += update[math.floor(len(update)/2)] if correct else 0

    return str(answer)
print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())