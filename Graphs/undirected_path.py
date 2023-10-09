'''
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
'''

# My Solution

from collections import deque

def undirected_path(edges, node_A, node_B):
  graph = {}
  
  for edge in edges:
    if edge[0] not in graph:
      graph[edge[0]] = [edge[1]]
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]   
      
    graph[edge[1]].append(edge[0]) 
    graph[edge[0]].append(edge[1])        
    
  visited = set()
  
  queue = deque([node_A])
  
  while queue:
    current = queue.popleft()
    
    if current == node_B:
      return True
    
    if current in visited:
      continue
    else:
      visited.add(current)
      for neighbor in graph[current]:
        queue.append(neighbor)
  
  return False
 
# Instructors Solution

# Recursive

def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
    
def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False

'''
n = number of nodes
e = number edges
Time: O(e)
Space: O(e)
'''

# Test Cases

# Test 0

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True

# Test 1

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'm', 'j') # -> True

# Test 2

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'l', 'j') # -> True

# Test 3

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'k', 'o') # -> False

# Test 4

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'i', 'o') # -> False

# Test 5

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'a', 'b') # -> True

# Test 6

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'a', 'c') # -> True

# Test 7

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 't') # -> True

# Test 8

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 'b') # -> False

# Test 9

edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]

undirected_path(edges, 'r', 't') # -> True
