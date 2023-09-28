'''
Write a function, is_univalue_list, that takes in the head of a linked list as an argument. 
The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  current = head.next
  while current != None:
    if current.val != head.val:
      return False
    current = current.next
  return True

# Instructors Solution

# Iterative

def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''

# Recursive

def is_univalue_list(head, prev_val = None):
  if head is None:
    return True
  if prev_val is None or head.val == prev_val:
    return is_univalue_list(head.next, head.val)
  else:
    return False

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

is_univalue_list(a) # True

# Test 1

a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

is_univalue_list(a) # False

# Test 2

u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

is_univalue_list(u) # True

# Test 3

u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 3 -> 3 -> 2

is_univalue_list(u) # False

# Test 4

z = Node('z')

# z

is_univalue_list(z) # True
