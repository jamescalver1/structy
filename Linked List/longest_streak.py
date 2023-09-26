'''
Write a function, longest_streak, that takes in the head of a linked list as an argument. 
The function should return the length of the longest consecutive streak of the same value within the list.
'''

# My Solution

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  max_streak = 0
  current_streak = 0
  prev_val = None
  current = head
  
  while current != None:
    
    if prev_val == current.val:
      current_streak += 1
    
    if prev_val != current.val:
      prev_val = current.val
      current_streak = 1
    
    if current_streak > max_streak:
      max_streak = current_streak
    
    current = current.next
  
  return max_streak

# Instructors Solution

# Iterative

def longest_streak(head):
  max_streak = 0
  current_streak = 0
  prev_val = None
  
  current_node = head
  while current_node is not None:
    if current_node.val == prev_val:
      current_streak += 1
    else:
      current_streak = 1
  
    prev_val = current_node.val
    if current_streak > max_streak:
      max_streak = current_streak
    
    current_node = current_node.next
    
  return max_streak

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''
