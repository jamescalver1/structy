'''
Write a function, has_path, that takes in a dictionary representing the adjacency 
list of a directed acyclic graph and two nodes (src, dst). The function should return a 
boolean indicating whether or not there exists a directed path between the source and destination nodes.
'''

# My Solution

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for node in graph[src]:
    if has_path(graph, node, dst):
      return True
  
  return False


# Instructors Solution

# Iterative

from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False

'''
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
'''

# Recursive

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False

'''
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
'''

# Test Cases

# Test 0

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True

# Test 1

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'j') # False

# Test 2

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'i', 'h') # True

# Test 3

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'w') # True

# Test 4

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'z') # False
