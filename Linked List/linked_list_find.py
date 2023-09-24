'''
Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
The function should return a list containing all values of the nodes in the linked list.
'''

# My Solution

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False


# Instructors Solution

# Iterative

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''

def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

# Recursive

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)