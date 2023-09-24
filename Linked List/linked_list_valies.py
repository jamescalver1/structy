'''
Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
The function should return a list containing all values of the nodes in the linked list.
'''

# My Solution

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  output = []
  current = head
  
  while current is not None:
    output.append(current.val)
    current = current.next
  
  return output

# Instructors Solution

# Iterative

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

# Recursive

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)