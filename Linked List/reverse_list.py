'''
Write a function, reverse_list, that takes in the head of a linked list as an argument. 
The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
'''

# My Solution

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head):
  previous = None
  current = head
  
  while current != None:
    next = current.next
    current.next = previous
    previous = current
    current = next
  
  return previous

# Instructors Solution

# Iterative

'''
n = number of nodes
Time: O(n)
Space: O(1)
'''

def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

# Recursive

'''
n = number of nodes
Time: O(n)
Space: O(n)
'''

def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)

# Test Cases

# Test 0

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

reverse_list(a) # f -> e -> d -> c -> b -> a

# Test 1

x = Node("x")
y = Node("y")

x.next = y

# x -> y

reverse_list(x) # y -> x

# Test 2

p = Node("p")

# p

reverse_list(p) # p
