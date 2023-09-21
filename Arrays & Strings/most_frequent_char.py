'''
most frequent char
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
'''

# My Solution
# Note that Max returns the first element in cases of a tie

from collections import Counter

def most_frequent_char(s):
  hash_map = Counter(s)
  return max(hash_map, key=hash_map.get)

# Instructors Solution
'''
n = length of string
Time: O(n)
Space: O(n)
'''

from collections import Counter

def most_frequent_char(s):
  count = Counter(s)
  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best