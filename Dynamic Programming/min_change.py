'''
Write a function min_change that takes in an amount and a list of coins. 
The function should return the minimum number of coins required to create the amount. 
You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.
'''

# My Solution

def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
    return -1
  else:
    return ans


def _min_change(amount, coins, memo):
  
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return 0
  
  if amount < 0:
    return float('inf')
  
  min_coins = float('inf')
  
  for num in coins:
    result = 1 + _min_change(amount - num, coins, memo)
    min_coins = min(min_coins, result)

  memo[amount] = min_coins
  return min_coins

# Instructors Solution

def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
    return -1
  else:
    return ans

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return 0
  
  if amount < 0:
    return float('inf')
  
  min_coins = float('inf')
  for coin in coins:
    num_coins = 1 + _min_change(amount - coin, coins, memo)
    min_coins = min(min_coins, num_coins)
    
  memo[amount] = min_coins
  return min_coins

# Recursive

'''
a = amount
c = # coins
Time: O(a*c)
Space: O(a)
'''

# Test Cases

# Test 0

min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible

# Test 1

min_change(13, [1, 9, 5, 14, 30]) # -> 5

# Test 2

min_change(23, [2, 5, 7]) # -> 4

# Test 3

min_change(2017, [4, 2, 10]) # -> -1

# Test 4

min_change(271, [10, 8, 265, 24]) # -> -1

# Test 5

min_change(0, [4, 2, 10]) # -> 0

# Test 6

min_change(0, []) # -> 0
