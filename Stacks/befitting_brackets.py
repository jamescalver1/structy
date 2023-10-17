'''
Write a function, befitting_brackets, that takes in a string as an argument. 
The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }
'''

# My Solution

def befitting_brackets(string):
  brackets = {
    ")" : "(",
    "]" : "[",
    "}" : "{"
  }
  
  stack = []
  
  for i in string:
    
    if i in brackets.values():
      stack.append(i)
    
    if i in brackets:
      if not stack:
        return False
      
      j = stack.pop()
      
      if j == brackets[i]:
        continue
      else:
        return False
    
  if stack:
    return False
  return True


# Instructors Solution

# Iterative

def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False
      
  return len(stack) == 0

'''
n = length of string
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

befitting_brackets('(){}[](())') # -> True

# Test 1

befitting_brackets('[][}') # -> False

# Test 2

befitting_brackets('[]{}(}[]') # -> False

# Test 3

befitting_brackets(']{}') # -> False

# Test 4

befitting_brackets('') # -> True

# Test 5

befitting_brackets('{[]}({}') # -> False
