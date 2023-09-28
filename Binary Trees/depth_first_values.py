'''
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in depth-first order.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
  stack = [root]
  values = []
  
  if root is None:
    return values

  while stack:
    cur = stack.pop()
    values.append(cur.val)
    
    if cur.right is not None:
      stack.append(cur.right)
      
    if cur.left is not None:
      stack.append(cur.left)

# Instructors Solution

# Iterative

def depth_first_values(root):
  if not root:
    return []
  
  stack = [root]
  values = []
  
  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Recursive

def depth_first_values(root):
  if not root:
    return []
  
  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [ root.val, *left_values, *right_values ]

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
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

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

# Test 1

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

# Test 2

a = Node('a')
#     a
depth_first_values(a) 
#   -> ['a']

# Test 3

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b
b.left = c
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#       \
#        d
#         \
#          e

depth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e']

# Test 4

depth_first_values(None) 
#   -> []
