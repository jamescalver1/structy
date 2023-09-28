'''
Write a function, longest_streak, that takes in the head of a linked list as an argument. 
The function should return the length of the longest consecutive streak of the same value within the list.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

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

# Test Cases

# Test 0

a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a) # 3

# Test 1

a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 3 -> 3 -> 3 -> 9 -> 9

longest_streak(a) # 4

# Test 2

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

longest_streak(a) # 3

# Test 3

a = Node(5)
b = Node(5)

a.next = b

# 5 -> 5

longest_streak(a) # 2

# Test 4

a = Node(4)

# 4

longest_streak(a) # 1

# Test 5

longest_streak(None) # 0
