'''
Write a function, breadth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in breadth-first order.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
  queue = [root]
  output = []
  
  while queue != [] and root != None:
    cur = queue.pop()
    output.append(cur.val)
    
    if cur.left is not None:
      queue.insert(0, cur.left)
      
    if cur.right is not None:
      queue.insert(0, cur.right)
  
  return output

# Instructors Solution

# Iterative

from collections import deque

def breadth_first_values(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values

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

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

# Test 1

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

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

breadth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Test 2

a = Node('a')

#      a

breadth_first_values(a) 
#    -> ['a']

# Test 3

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']

# Test 4

breadth_first_values(None) 
#    -> []
