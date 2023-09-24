'''
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
The function should return the total sum of all values in the linked list.
'''

# My Solution

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  value = 0
  current = head
  while current is not None:
    value += current.val
    current = current.next
    
  return value


# Instructors Solution

# Iterative

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''

def sum_list(head):
  total_sum = 0
  current = head
  while current is not None:
    total_sum += current.val
    current = current.next
  return total_sum

# Recursive

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
