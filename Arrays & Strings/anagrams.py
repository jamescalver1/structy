'''
anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
'''

# My Solution

def anagrams(s1, s2):
  if len(s1) != len(s2):
    return False
  
  hash_1 = {}
  hash_2 = {}
  
  for i, j in zip(s1, s2):
    if i not in hash_1:
      hash_1[i] = 1
    else:
      hash_1[i] += 1
    
    if j not in hash_2:
      hash_2[j] = 1
    else:
      hash_2[j] += 1
      
  if hash_1 == hash_2:
    return True
  return False

# Instructors Solution
# The Counter function from collections creates the hash map counting each element
# A cleaner solution to the above would be to create a helper function to for creating the hash maps
'''
n = length of string 1
m = length of string 2
Time: O(n + m)
Space: O(n + m)
'''

from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)
