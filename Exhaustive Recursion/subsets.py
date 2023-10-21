'''
Write a function, subsets, that takes in a list as an argument. 
The function should return a 2D list where each sublist represents one of the possible subsets of the list.

The elements within the subsets and the subsets themselves may be returned in any order.

You may assume that the input list contains unique elements.
'''

# My Solution

def subsets(elements):
  if len(elements) == 0:
    return [[]]
  
  first = elements[0]
  subs_without_first = subsets(elements[1:])
  
  sub_with_first = []
  for sub in subs_without_first:
    sub_with_first.append([first, *sub])
  
  return subs_without_first + sub_with_first

# Instructors Solution

# Recursive

def subsets(elements):
  if not elements:
    return [[]]

  first = elements[0]
  remaining_elements = elements[1:]
  subsets_without_first = subsets(remaining_elements)

  subsets_with_first = []
  for sub in subsets_without_first:
    subsets_with_first.append([ first, *sub ])

  return subsets_without_first + subsets_with_first

'''
n = length of elements array
Time: ~O(2^n)
Space: ~O(2^n)
'''

# Test Cases

# Test 0

subsets(['a', 'b']) # ->
# [ 
#   [], 
#   [ 'b' ], 
#   [ 'a' ], 
#   [ 'a', 'b' ] 
# ]

# Test 1

subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]

# Test 2

subsets(['x']) # ->
# [ 
#   [], 
#   [ 'x' ] 
# ]

# Test 3

subsets([]) # ->
# [ 
#   []
# ]

# Test 4

subsets(['q', 'r', 's', 't']) # ->
# [
#   [],
#   [ 't' ],
#   [ 's' ],
#   [ 's', 't' ],
#   [ 'r' ],
#   [ 'r', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 's', 't' ],
#   [ 'q' ],
#   [ 'q', 't' ],
#   [ 'q', 's' ],
#   [ 'q', 's', 't' ],
#   [ 'q', 'r' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 's', 't' ]
# ]
