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

    for n1,n2 in edges:
      self.data[n1].append(n2)
      self.data[n2].append(n1)

  def __repr__(self):
    return "\n".join(["{} : {}".format(n,neighbor) for n,neighbor in enumerate(self.data)])

  def __str__(self):
    return self.__repr__()


def dfs(graph,root):
  stack = []
  visited = [False] * len(graph.data)
  distance = [None] * len(graph.data)
  parent = [None] * len(graph.data)
  result = []

  stack.append(root)
  distance[root] = 0

  while len(stack) > 0:
    current = stack.pop()

    if not visited[current]:
      visited[current] = True
      result.append(current)

      for node in graph.data[current]:
        if not visited[node]:
          stack.append(node)
          distance[node] = distance[current] + 1
          parent[node] = current


  return result, distance, parent


print(Graph(**graph0['input']))
print(dfs(Graph(**graph0['input']),3))



