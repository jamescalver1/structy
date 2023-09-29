'''
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
The function should return the total sum of all values in the tree.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_sum(root):
  sum = 0
  stack = [root]
  
  while stack != [] and root is not None:
    curr = stack.pop()
    sum += curr.val
    
    if curr.left is not None:
      stack.append(curr.left)
      
    if curr.right is not None:
      stack.append(curr.right)
    
  return sum

# Instructors Solution

# Iterative

from collections import deque

def tree_sum(root):
  if not root:
    return 0

  queue = deque([ root ])
  total_sum = 0
  while queue:
    node = queue.popleft()

    total_sum += node.val

    if node.left:
      queue.append(node.left)

    if node.right:
      queue.append(node.right)

  return total_sum

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Recursive

def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

tree_sum(a) # -> 21

# Test 1

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

tree_sum(a) # -> 10

# Test 2

tree_sum(None) # -> 0
