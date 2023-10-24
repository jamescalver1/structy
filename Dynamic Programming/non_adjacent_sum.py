'''
Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. 
The function should return the maximum sum of non-adjacent items in the list. 
There is no limit on how many items can be taken into the sum as long as they are not adjacent.
'''

# My Solution

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, {})


def _non_adjacent_sum(nums, memo):
  if str(nums) in memo:
    return memo[str(nums)]

  if nums == []:
    return 0
  
  if len(nums) == 1:
    return nums[0]
  
  l = nums[2:]
  r = nums[1:]
  
  l_result = nums[0] + _non_adjacent_sum(l, memo)
  r_result = _non_adjacent_sum(r, memo)
  
  memo[str(nums)] = max(l_result, r_result)
  
  return memo[str(nums)]


# Instructors Solution

# Recursive

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i in memo:
    return memo[i]
  
  if i >= len(nums):
    return 0
  
  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)
  return memo[i]

'''
n = length of nums
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

nums = [2, 4, 5, 12, 7]
non_adjacent_sum(nums) # -> 16

# Test 1

nums = [7, 5, 5, 12]
non_adjacent_sum(nums) # -> 19

# Test 2

nums = [7, 5, 5, 12, 17, 29]
non_adjacent_sum(nums) # -> 48

# Test 3

nums = [
  72, 62, 10,  6, 20, 19, 42,
  46, 24, 78, 30, 41, 75, 38,
  23, 28, 66, 55, 12, 17, 9,
  12, 3, 1, 19, 30, 50, 20
]
non_adjacent_sum(nums) # -> 488

# Test 4

nums = [
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
  61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  42
]
non_adjacent_sum(nums) # -> 1465
