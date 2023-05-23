graph0 = {
  'input' : {
    'num_nodes' : 5,
    'edges' : [(0,1), (0,4), (1,2), (1,3), (1,4), (4,3), (3,2)]
  }
}

graph1 = {
  'input' : {
    'num_nodes' : 6,  
    'edges' : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
  }
}

graph2 = {
  'input' : {
    'num_nodes' : 8,  
    'edges' : [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
  }
}

graph3 = {
  'input' : {
    'num_nodes' : 6,
    'edges' : [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
  }
}

class Graph:
  def __init__(self, num_nodes, edges):

    self.num_nodes = num_nodes
    self.data = [[] for _ in range(num_nodes)]

    for n1, n2 in edges:
      self.data[n1].append(n2)
      self.data[n2].append(n1)
  
  def __repr__(self):
    return "\n".join(["{} : {}".format(n, neighbor) for n, neighbor in enumerate(self.data)])

  def __str__(self):
    return self.__repr__()

print("----------------TEST-1-------------------")

print(Graph(**graph0['input']))

def bfs(graph, root):
  queue = []
  visited = [False] * len(graph.data)
  distance = [None] * len(graph.data)
  parent = [None] * len(graph.data)

  visited[root] = True
  distance[root] = 0
  queue.append(root)
  idx = 0

  while idx < len(queue):
    current = queue[idx]
    idx += 1

    for node in graph.data[current]:
      if not visited[node]:
        visited[node] = True
        distance[node] = distance[current] + 1
        parent[node] = current
        queue.append(node)

  return queue, parent, distance

print(end="\n")

print(bfs(Graph(**graph0['input']),1))

print("-----------------------------------------")

print("----------------TEST-2-------------------")

print(Graph(**graph1['input']))

print(end="\n")

print(bfs(Graph(**graph1['input']),1))

print("-----------------------------------------")

print("----------------TEST-3-------------------")

print(Graph(**graph2['input']))

print(end="\n")

print(bfs(Graph(**graph2['input']),1))

print("-----------------------------------------")

print("----------------TEST-4-------------------")

print(Graph(**graph3['input']))

print(end="\n")

print(bfs(Graph(**graph3['input']),1))

print("-----------------------------------------")

