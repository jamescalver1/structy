'''
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
'''

# My Solution

def intersection(a, b):
  items = set(a)
  output = []
  
  for num in b:
    if num in items:
      output.append(num)
  
  return output

# Instructors Solution
'''
n = length of array a, m = length of array b
Time: O(n+m)
Space: O(n)
'''

def intersection(a, b):
  set_a = set(a)
  return [ item for item in b if item in set_a ]