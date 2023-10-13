'''
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
'''

# My Solution

def fib(n):
  memo = {}
  return _fib(n, memo)


def _fib(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  if n == 1:
    return 1
  
  result = _fib(n - 1, memo) + _fib(n - 2, memo)
  memo[n] = result
  
  return memo[n]

# Instructors Solution

# Recursive

def fib(n):
  memo = {}
  return _fib(n, memo)

def _fib(n, memo):
  if n == 0 or n == 1:
    return n
  
  if n in memo:
    return memo[n]

  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
  return memo[n]

'''
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

fib(0) # -> 0

# Test 1

fib(1) # -> 1

# Test 2

fib(5) # -> 5

# Test 3

fib(35) # -> 9227465

# Test 4

fib(46) # -> 1836311903
