'''
Write a function, count_paths, that takes in a grid as an argument. 
In the grid, 'X' represents walls and 'O' represents open spaces. 
You may only move down or to the right and cannot pass through walls. 
The function should return the number of ways possible to travel from the top-left 
corner of the grid to the bottom-right corner.
'''

# My Solution

def count_paths(grid):
  memo = {}
  position = (0,0)
  
  if grid[len(grid) -1][len(grid[0]) -1] == "X":
    return 0
  
  return _count_paths(position, grid, memo)


def _count_paths(position, grid, memo):
  if position in memo:
    return memo[position]
  
  if position == (len(grid) -1, len(grid[0]) -1):
    return 1
  
  if position[0] > len(grid) -1 or position[1] > len(grid[0]) -1:
    return 0

  if grid[position[0]][position[1]] == "X":
    return 0
  
  down_position = (position[0] + 1, position[1])
  down_result = _count_paths(down_position, grid, memo)
  
  right_position = (position[0], position[1] + 1)
  right_result = _count_paths(right_position, grid, memo)
  
  memo[position] = down_result + right_result
  
  return memo[position]

# Instructors Solution

# Recursive

def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
    return 0
  
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1
  
  memo[pos] = _count_paths(grid, r + 1, c, memo) + _count_paths(grid, r, c + 1, memo)
  return memo[pos]

'''
r = # rows
c = # columns
Time: O(r*c)
Space: O(r*c)
'''

# Test Cases

# Test 0

grid = [
  ["O", "O"],
  ["O", "O"],
]
count_paths(grid) # -> 2

# Test 1

grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 5

# Test 2

grid = [
  ["O", "O", "O"],
  ["O", "O", "X"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 3

# Test 3

grid = [
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 1

# Test 4

grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "X", "O", "O", "O"],
  ["X", "O", "X", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
count_paths(grid) # -> 0

# Test 5

grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
count_paths(grid) # -> 42
