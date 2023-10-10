'''
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.
'''

# My Solution

from collections import deque

def connected_components_count(graph):
  components = 0
  visited = set()
  
  for node in graph:
    
    if node in visited:
      continue
    
    queue = deque([node])
    
    while queue:
      current = queue.popleft()
      visited.add(current)
      
      for neighbour in graph[current]:
        if neighbour in visited:
          continue
        queue.append(neighbour)
        visited.add(neighbour)
    
    components += 1
    
  return components

# Instructors Solution

# Recursive

def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
      
  return count

def explore(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  
  return True

'''
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
'''

# Test Cases

# Test 0

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2

# Test 1

connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 1

# Test 2

connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 3

# Test 3

connected_components_count({}) # -> 0

# Test 4

connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 5
