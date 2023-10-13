'''
Write a function sum_possible that takes in an amount and a list of positive numbers. 
The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. 
You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
'''

# My Solution

def sum_possible(amount, numbers):
  memo = {}
  
  if amount == 0:
    return True
  
  if not numbers:
    return False
  
  return _sum_possible(amount, numbers, memo)


def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return True
  
  if amount == 1:
    return False
  
  if min(numbers) > amount:
    return False
  
  result = set()
  
  for num in numbers:
    outcome = _sum_possible(amount - num, numbers, memo)
    result.add(outcome)
  
  if True in result:
    memo[amount] = True
  else:
    memo[amount] = False
    
  return memo[amount]


# Instructors Solution

# Recursive

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount < 0:
    return False
  
  if amount == 0:
    return True
  
  for num in numbers:
    if _sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
    
  memo[amount] = False  
  return False

'''
a = amount
n = length of numbers
Time: O(a*n)
Space: O(a)
'''

# Test Cases

# Test 0

sum_possible(8, [5, 12, 4]) # -> True, 4 + 4

# Test 1

sum_possible(15, [6, 2, 10, 19]) # -> False

# Test 2

sum_possible(103, [6, 20, 1]) # -> True

# Test 3

sum_possible(0, []) # -> True

# Test 4

sum_possible(12, []) # -> False

# Test 5

sum_possible(2017, [4, 2, 10]) # -> False
