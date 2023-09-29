'''
Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
The function should return a boolean indicating whether or not the value is contained in the tree.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_includes(root, target):
  s = [root]
  r = False
  
  while s != [] and root is not None:
    c = s.pop()
    
    if c.val == target:
      r = True
      break
    
    if c.right is not None:
      s.append(c.right)
    if c.left is not None:
      s.append(c.left)
  
  return r

# Instructors Solution

# Iterative

from collections import deque

def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque([ root ])
  
  while queue:
    node = queue.popleft()
    
    if node.val == target:
      return True
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return False

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Recursive

def tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)

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

tree_includes(a, "e") # -> True

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
tree_includes(a, "a") # -> True

# Test 2

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

tree_includes(a, "n") # -> False

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

tree_includes(a, "f") # -> True

# Test 4

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

tree_includes(a, "p") # -> False

# Test 5

tree_includes(None, "b") # -> False
