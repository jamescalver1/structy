'''
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
'''

# My Solution

def pair_product(numbers, target_product):
  map = {}
  for (i, num) in enumerate(numbers):
    com = target_product / num
    if com in map:
      return (map[com], i)
    map[num] = i

# Instructors Solution
'''
n = length of numbers list
Time: O(n)
Space: O(n)
'''

def pair_product(numbers, target_product):
  previous_nums = {}
  
  for index, num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_nums:
      return (index, previous_nums[complement])
    
    previous_nums[num] = index
