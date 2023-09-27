'''
Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. 
The function should return the head of the linked list.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  dummy = Node(None)
  tail = dummy
  
  for val in values:
    node = Node(val)
    tail.next = node
    tail = node
    
  return dummy.next

# Instructors Solution

# Iterative

def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next

'''
n = length of values
Time: O(n)
Space: O(n)
'''

# Recursive

def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head

'''
n = length of values
Time: O(n)
Space: O(n)
'''

# Test Cases

# Test 0

create_linked_list(["h", "e", "y"])
# h -> e -> y

# Test 1

create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8

# Test 2

create_linked_list(["a"])
# a

# Test 3

create_linked_list([])
# null
