'''
Write a function, create_combinations, that takes in a list and a length as arguments. 
The function should return a 2D list representing all of the combinations of the specifized length.

The items within the combinations and the combinations themselves may be returned in any order.

You may assume that the input list contains unique elements and 1 <= k <= len(items).
'''

# My Solution

def create_combinations(items, k):
  if k == 0:
    return [[]]
  
  if k > len(items):
    return []
  
  first = items[0]
  combinations = create_combinations(items[1:], k)
  reduced_combinations = create_combinations(items[1:], k - 1)
  
  result = []
  for combo in reduced_combinations:
    result.append([first, *combo])
  
  return combinations + result

# Instructors Solution

# Recursive

def create_combinations(items, k):
  if len(items) < k:
    return []
  
  if k == 0:
    return [[]]
  
  first = items[0]
  combos_with_first = []
  for combo in create_combinations(items[1:], k - 1):
    combos_with_first.append([ first, *combo ])
  
  combos_without_first = create_combinations(items[1:], k)
  
  return combos_with_first + combos_without_first

'''
n = length of items
k = target length
Time: ~O(n choose k)
Space: ~O(n choose k)
'''

# Test Cases

# Test 0

create_combinations(["a", "b", "c"], 2); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]

# Test 1

create_combinations(["q", "r", "s", "t"], 2) # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]

# Test 2

create_combinations(['q', 'r', 's', 't'], 3) # ->
# [
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 's', 't' ],
#   [ 'r', 's', 't' ]
# ]

# Test 3

create_combinations([1, 28, 94], 3) # ->
# [
#   [ 1, 28, 94 ]
# ]
