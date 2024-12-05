with open('Data/Day04Data.txt', 'r') as file:
    grid = list(map(str.strip, file))

def part1():
    xmasAmount = 0
    # Loop over the 2d array
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Check if theres an X at current index
            if grid[row][column] == 'X':
                # Loop over all the directions to look
                for direction in [{'r': -1, 'c': 0}, {'r': -1, 'c': 1}, {'r': 0, 'c': 1}, {'r': 1, 'c': 1}, {'r': 1, 'c': 0}, {'r': 1, 'c': -1}, {'r': 0, 'c': -1}, {'r': -1, 'c': -1}]:
                    # Check if the selected direction from the current index will be in the grid
                    if 0 <= row + (direction['r'] * 3) < len(grid) and 0 <= column + (direction['c'] * 3) < len(grid[0]):
                        # Check for the remaining letters using the direction
                        if grid[row + direction['r']][column + direction['c']] == "M" and grid[row + (direction['r'] * 2)][column + (direction['c'] * 2)] == "A" and grid[row + (direction['r'] * 3)][column + (direction['c'] * 3)] == "S":
                            xmasAmount += 1
    return str(xmasAmount)
    
def part2():
    xmasCrossAmount = 0
    # Loop over the 2d array
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            outOfBounds = False
            for checkDir in [{'r': 1, 'c': -1}, {'r': -1, 'c':-1}, {'r': 1, 'c': 1}, {'r': -1, 'c':1}]:
                # Check if any directions are out of bounds
                if row + checkDir['r'] < 0 or row + checkDir['r'] >= len(grid) or column + checkDir['c'] < 0 or column + checkDir['c'] >= len(grid[0]):
                    outOfBounds = True
                    continue
            # Check if theres an A at current index
            if not outOfBounds and grid[row][column] == 'A':
                correctAmount = 0
                # Loop over top left and bottom left to check for an A or an S
                for direction in [{'r': 1, 'c': -1}, {'r': -1, 'c':-1}]:
                    # Check for A
                    if grid[row + direction['r']][column + direction['c']] == "M":
                        if grid[row - direction['r']][column - direction['c']] == "S":
                            correctAmount += 1
                        # Check if the reversed side is S
                    # Check for S
                    elif grid[row + direction['r']][column + direction['c']] == "S":
                        # Check if the reversed side is A
                        if grid[row - direction['r']][column - direction['c']] == "M":
                            correctAmount += 1
                # If both were correct, add to answer
                if correctAmount == 2:
                    xmasCrossAmount += 1
    return str(xmasCrossAmount)
print("Part 1 answer: " + part1())
print("Part 2 answer: " + part2())