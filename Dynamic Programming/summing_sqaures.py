'''
Write a function, summing_squares, that takes a target number as an argument. 
The function should return the minimum number of perfect squares that sum to the target. 
A perfect square is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
'''

# My Solution

def summing_squares(n):
  squares = [1]
  
  cnt = 2
  while max(squares) < n:
    squares.append(cnt * cnt)
    cnt += 1
  
  return _summing_squares(n, squares, {})


def _summing_squares(n, squares, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  result = []
  
  for sqr in squares:
    if sqr > n:
      break
    result.append( 1 + _summing_squares(n - sqr, squares, memo))

  memo[n] = min(result)
  
  return memo[n]


# Instructors Solution

# Recursive

import math

def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n) + 1)):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)
  
  memo[n] = min_squares
  return min_squares

'''
n = length of nums
Time: O(n * sqrt(n))
Space: O(n)
'''

# Test Cases

# Test 0

summing_squares(8) # -> 2

# Test 1

summing_squares(9) # -> 1

# Test 2

summing_squares(12) # -> 3

# Test 3

summing_squares(1) # -> 1

# Test 4

summing_squares(31) # -> 4

# Test 5

summing_squares(50) # -> 2

# Test 6

summing_squares(68) # -> 2

# Test 7

summing_squares(87) # -> 4