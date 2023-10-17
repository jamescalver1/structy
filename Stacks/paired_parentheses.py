'''
Write a function, paired_parentheses, that takes in a string as an argument. 
The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.
'''

# My Solution

def paired_parentheses(string):
  stack = []
  for i in string:
    
    if i == "(":
      stack.append(i)
    
    if i == ")":
      if not stack:
        return False
      stack.pop()
      continue
  
  if not stack:
    return True
  return False


# Instructors Solution

# Iterative

def paired_parentheses(string):
  count = 0
  
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1
      
  return count == 0

'''
n = length of string
Time: O(n)
Space: O(1)
'''

# Test Cases

# Test 0

paired_parentheses("(david)((abby))") # -> True

# Test 1

paired_parentheses(")(") # -> False

# Test 2

paired_parentheses("(())(water()()") # -> False

# Test 3

paired_parentheses("") # -> True

# Test 4

paired_parentheses("()") # -> True

# Test 5

paired_parentheses("()rose(jeff") # -> False
