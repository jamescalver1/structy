'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.
'''

# My Solution

from collections import deque

def largest_component(graph):
  max = 0
  visited = set()
  
  for node in graph:
    
    if node in visited:
      continue
    
    queue = deque([node])
    size = 0
    
    while queue:
      current = queue.popleft()
      visited.add(current)
      
      for neighbour in graph[current]:
        if neighbour in visited:
          continue
        queue.append(neighbour)
        visited.add(neighbour)
    
      size += 1
    
    if size > max:
      max = size
  
  return max

# Instructors Solution

# Recursive

def largest_component(graph):
  visited = set()
  
  largest = 0
  for node in graph:
    size = explore_size(graph, node, visited)
    if size > largest:
      largest = size
  
  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0
  
  visited.add(node)
  
  size = 1
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)
    
  return size

'''
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
'''

# Test Cases

# Test 0

largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

# Test 1

largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6

# Test 2

largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 5

# Test 3

largest_component({}) # -> 0

# Test 4

largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 3
