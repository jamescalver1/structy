'''
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. 
The function should insert a new node with the value into the list at the specified index. 
Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  node = Node(value)
  count = 0
  current = head
  
  if index == 0:
    node.next = current
    return node
  
  while count != index - 1:
    current = current.next
    count += 1
  
  node.next = current.next
  current.next = node
  
  return head

# Instructors Solution

# Iterative

def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head
    
  count = 0
  current = head
  while current is not None:
    if count == index - 1:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
    
    count += 1
    current = current.next
  return head

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''

# Recursive

def insert_node(head, value, index, count = 0):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head
  
  if head is None:
    return None
  
  if count == index - 1:
      temp = head.next
      head.next = Node(value)
      head.next.next = temp
      return 
  
  insert_node(head.next, value, index, count + 1)
  return head

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

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'x', 2)
# a -> b -> x -> c -> d

# Test 1

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'v', 3)
# a -> b -> c -> v -> d

# Test 2

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'm', 4)
# a -> b -> c -> d -> m

# Test 3

a = Node("a")
b = Node("b")

a.next = b

# a -> b

insert_node(a, 'z', 0)
# z -> a -> b
