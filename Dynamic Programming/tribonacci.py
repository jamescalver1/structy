'''
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
'''

# My Solution

def tribonacci(n):
  memo = {}
  return _tribonacci(n, memo)


def _tribonacci(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0 or n == 1:
    return 0
  
  if n == 2:
    return 1
  
  result = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
  memo[n] = result
  
  return memo[n]

# Instructors Solution

# Recursive

def tribonacci(n):
  return _tribonacci(n, {})

def _tribonacci(n, memo):
  if n in memo:
    return memo[n]

  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
  return memo[n]

'''
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

tribonacci(0) # -> 0

# Test 1

tribonacci(1) # -> 0

# Test 2

tribonacci(2) # -> 1

# Test 3

tribonacci(5) # -> 4

# Test 4

tribonacci(20) # -> 35890

# Test 5

tribonacci(37) # -> 1132436852
