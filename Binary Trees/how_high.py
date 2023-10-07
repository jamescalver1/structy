'''
Write a function, how_high, that takes in the root of a binary tree. 
The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def how_high(node):
  if not node:
    return -1
  
  return max(how_high(node.left), how_high(node.right)) + 1

# Instructors Solution

# Recursive

def how_high(node):
  if node is None:
    return -1

  left_height = how_high(node.left)
  right_height = how_high(node.right)
  return 1 + max(left_height, right_height)

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

how_high(a) # -> 2

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

how_high(a) # -> 3

# Test 2

a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

how_high(a) # -> 1

# Test 3

a = Node('a')

#      a

how_high(a) # -> 0

# Test 4

how_high(None) # -> -1
