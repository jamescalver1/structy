'''
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
The function should return the length of the longest path within the graph. A path may start and end at any two nodes. 
The length of a path is considered the number of edges in the path, not the number of nodes.
'''

# My Solution

def longest_path(graph):
  distance = {}
  
  for node in graph:
    if not graph[node]:
      distance[node] = 0
  
  for node in graph:
    traverse_distance(graph, node, distance)
  
  return max(distance.values())
    
def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  max_length = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > max_length:
      max_length = attempt
  
  distance[node] = 1 + max_length
  return distance[node]


# Instructors Solution

# Recursive

def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
      
  for node in graph:
    traverse_distance(graph, node, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]

'''
e = # edges
n = # nodes
Time: O(e)
Space: O(n)
'''

# Test Cases

# Test 0

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2

# Test 1

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

longest_path(graph) # -> 4

# Test 2

graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

longest_path(graph) # -> 2

# Test 3

graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}

longest_path(graph) # -> 3
