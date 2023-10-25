'''
Write a function, counting_change, that takes in an amount and a list of coins. 
The function should return the number of different ways it is possible to make 
change for the given amount using the coins.

You may reuse a coin as many times as necessary.
'''

# My Solution

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  total_ways = 0
  coin = coins[i]
  
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_ways
  
  return memo[key]


# Instructors Solution

# Recursive

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  coin = coins[i]
  
  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_count
  return total_count

'''
a = amount
c = # coins
Time: O(a*c)
Space: O(a*c)
'''

# Test Cases

# Test 0

counting_change(4, [1, 2, 3]) # -> 4

# Test 1

counting_change(8, [1, 2, 3]) # -> 10

# Test 2

counting_change(24, [5, 7, 3]) # -> 5

# Test 3

counting_change(13, [2, 6, 12, 10]) # -> 0

# Test 4

counting_change(512, [1, 5, 10, 25]) # -> 20119

# Test 5

counting_change(1000, [1, 5, 10, 25]) # -> 142511

# Test 6

counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # -> 1525987916
