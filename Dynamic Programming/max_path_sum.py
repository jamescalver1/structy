'''
Write a function, max_path_sum, that takes in a grid as an argument. 
The function should return the maximum sum possible by traveling a path 
from the top-left corner to the bottom-right corner. You may only travel 
through the grid by moving down or right.

You can assume that all numbers are non-negative.
'''

# My Solution

def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, r, c, memo):
  pos = (r, c)
  
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) -1 and c == len(grid[0]) -1:
    return grid[r][c]
  
  if r > len(grid) - 1 or c > len(grid[0]) -1:
    return float('-inf')
  
  down_result = _max_path_sum(grid, r +1, c, memo)
  right_result = _max_path_sum(grid, r, c +1, memo)
  
  memo[pos] = grid[r][c] + max(down_result, right_result)
  
  return memo[pos]


# Instructors Solution

# Recursive

def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) or c == len(grid[0]):
    return float('-inf')
  
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]
  
  down = _max_path_sum(grid, r + 1, c, memo)
  right = _max_path_sum(grid, r, c + 1, memo)  
  
  memo[pos] = grid[r][c] + max(down, right)
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
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
max_path_sum(grid) # -> 18

# Test 1

grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
max_path_sum(grid) # -> 36

# Test 2

grid = [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
max_path_sum(grid) # -> 39

# Test 3

grid = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
max_path_sum(grid) # -> 27

# Test 4

grid = [
  [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 42, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
max_path_sum(grid) # -> 82
