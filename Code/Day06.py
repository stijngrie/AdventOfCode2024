import math

with open('Data/Day06Data.txt', 'r') as file:
    grid = list(map(str.strip, file))

# Create array of directions the guard can loop through
directions = [{'r': -1, 'c': 0}, {'r': 0, 'c': 1}, {'r': 1, 'c': 0}, {'r': 0, 'c': -1}]

for row in range(len(grid)):
    for column in range(len(grid[0])):
        if grid[row][column] == '^':
            startGuardPos = {'r': row, 'c': column, 'dr': directions[0]['r'], 'dc': directions[0]['c']}

def part1():
    # Create array of all unique positions the guard has visited
    uniquePositions = []
    currentDirection = directions[0]
    # Find the position of the guard
    guardPos = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == '^':
                guardPos = {'r': row, 'c': column}

    # Continue stepping until the guard is out of the area
    while True:
        # Put the current position in the array if it wasn't already
        if guardPos not in uniquePositions:
            uniquePositions.append(guardPos)
        # Get the next position
        nextPos = {'r': guardPos['r'] + currentDirection['r'], 'c': guardPos['c'] + currentDirection['c']}
        # Check if the next position is out of bounds
        if nextPos['r'] >= len(grid) or nextPos['r'] < 0 or nextPos['c'] < 0 or nextPos['c'] >= len(grid[0]):
            break

        # Check if the nextpos is an object, if true, rotate
        if grid[nextPos['r']][nextPos['c']] == '#':
            nextIndex = (directions.index(currentDirection) + 1) % len(directions)
            currentDirection = directions[nextIndex]
        else:
            guardPos = nextPos

    return str(len(uniquePositions))
    
def part2():
    answer = 0
    # Loop over all spots and pretend there is an object there to see if the guard loops
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            print(row * len(grid) + column, '/', len(grid) * len(grid[0]))
            answer += 1 if findLoop(row, column) else 0
    return str(answer)

def findLoop(objRow, objCol):
    # Create array of all unique positions the guard has visited
    uniquePositions = []
    currentDirection = directions[0]
    # Find the position of the guard
    guardPos = startGuardPos
    # Continue stepping until the guard is out of the area
    while True:
        # Put the current position in the array if it wasn't already
        if guardPos not in uniquePositions:
            uniquePositions.append(guardPos)
        else:
            return True
        # Get the next position
        nextPos = {'r': guardPos['r'] + currentDirection['r'], 'c': guardPos['c'] + currentDirection['c'], 'dr': currentDirection['r'], 'dc': currentDirection['c']}
        # Check if the next position is out of bounds
        if nextPos['r'] >= len(grid) or nextPos['r'] < 0 or nextPos['c'] < 0 or nextPos['c'] >= len(grid[0]):
            return False

        # Check if the nextpos is an object, if true, rotate
        if grid[nextPos['r']][nextPos['c']] == '#' or (nextPos['r'] == objRow and nextPos['c'] == objCol):
            nextIndex = (directions.index(currentDirection) + 1) % len(directions)
            currentDirection = directions[nextIndex]
            guardPos = {'r': guardPos['r'], 'c': guardPos['c'], 'dr': currentDirection['r'], 'dc': currentDirection['c']}
        else:
            guardPos = nextPos
                  
    
print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())