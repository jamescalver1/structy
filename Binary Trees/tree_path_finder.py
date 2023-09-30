'''
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value. 
If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  return result[::-1]

def _path_finder(root, target):
  
  if root is None:
    return None
  
  if root.val == target:
    return [target]

  left = _path_finder(root.left, target)
  if left is not None:
    left.append(root.val)
    return left
  
  right = _path_finder(root.right, target)
  if right is not None:
    right.append(root.val)
    return right
  
  return None

# Instructors Solution

# Recursive

def path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [ root.val, *left_path ]
  
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [ root.val, *right_path ]
  
  return None

'''
n = number of nodes
Time: O(n^2)
Space: O(n)
'''

# Recursive

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = _path_finder(root.left, target)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  
  return None

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]

# Test 1

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

path_finder(a, 'p') # -> None

# Test 2

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

path_finder(a, "c") # -> ['a', 'c']

# Test 3

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

path_finder(a, "h") # -> ['a', 'c', 'f', 'h']

# Test 4

x = Node("x")

#      x

path_finder(x, "x") # -> ['x']

# Test 5

path_finder(None, "x") # -> None

# Test 6

root = Node(0)
curr = root
for i in range(1, 19500):
  curr.right = Node(i)
  curr = curr.right

#      0
#       \
#        1
#         \
#          2
#           \
#            3
#             .
#              .
#               .
#              19498
#                \
#                19499

path_finder(root, 16281) # -> [0, 1, 2, 3, ..., 16280, 16281]
