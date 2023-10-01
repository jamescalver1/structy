'''
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
The function should return the number of times that the target occurs in the tree.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_value_count(root, target):

  if root is None:
    return 0
  
  if root.val == target:
    return 1 + tree_value_count(root.left, target) + tree_value_count(root.right, target)
  
  return 0 + tree_value_count(root.left, target) + tree_value_count(root.right, target)

# Instructors Solution

# Recursive

def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Iterative

def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  stack = [ root ]
  while stack:
    current = stack.pop()
    if current.val == target:
      count += 1

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return count

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Iterative

from collections import deque

def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0
  queue = deque([ root ])
  while queue:
    current = queue.popleft()
    if current.val == target:
      count += 1

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return count

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

tree_value_count(a,  6) # -> 3

# Test 1

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4  6     12

tree_value_count(a,  12) # -> 2

# Test 2

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

tree_value_count(a, 1) # -> 4

# Test 3

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

tree_value_count(a, 9) # -> 0

# Test 4

tree_value_count(None, 42) # -> 0
