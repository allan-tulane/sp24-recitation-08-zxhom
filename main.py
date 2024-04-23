from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

  def spath_helper(visited, frontier, edge):
    if len(frontier) == 0:
      print('FRONTIER EMPTY')
      return visited

    else:
      distance, edge, vertex = heappop(frontier)

      if vertex in visited:
        return spath_helper(visited, frontier, edge + 1)
      else:
        visited[vertex] = (distance, edge)
        print('visiting: ', vertex, 'with distance: ', distance, 'with edge',
              edge)

        for neighbor, weight in graph[vertex]:  # add all V/E to frontier
          heappush(frontier, (distance + weight, edge + 1, neighbor))

        return spath_helper(visited, frontier, edge + 1)

  visited = dict()
  frontier = []
  heappush(frontier, (0, 0, source))
  return spath_helper(visited, frontier, 0)


'''
def test_shortest_shortest_path():

  graph = {
      's': {('a', 1), ('c', 4)},
      'a': {('b', 2)},  # 'a': {'b'},
      'b': {('c', 1), ('d', 4)},
      'c': {('d', 3)},
      'd': {},
      'e': {('d', 0)}
  }
  result = shortest_shortest_path(graph, 's')
  print('result= ', result)


test_shortest_shortest_path()
'''


def bfs_path(graph, source):
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

  def bfs_helper(visited, frontier, last_parent):
    init = 0
    while len(frontier) > 0:
      vertex = heappop(frontier)
      init = vertex

      if vertex in visited:
        return bfs_helper(visited, frontier, last_parent)

      else:
        if last_parent == 0:  # First iteration case
          for neighbor in graph[vertex]:
            heappush(frontier, neighbor)  # b and c added to frontier
          return bfs_helper(visited, frontier, source)

        #for children in graph[last_parent]:
        visited[vertex] = last_parent
        #print('visiting: ', vertex, 'with parent: ', last_parent)

    # Outside of while loop
    if init == 0:
      return visited

    # takes the last in frontier as the next parent
    for neighbor in graph[
        init]:  # add newV to frontier once old frontier is empty
      heappush(frontier, neighbor)

    return bfs_helper(visited, frontier, init)

  visited = dict()
  frontier = []
  heappush(frontier, source)
  return bfs_helper(visited, frontier, 0)
  #{'a': 's', 'b': 's', 'c': 'b', 'd': 'c'}


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test case for example.
    """
  path = []

  while destination in parents:
    destination = parents[destination]
    path.insert(0, destination)
  return ''.join(path)

  # destination = get_path(parents, destination)
  # return destination




# x = get_path(parents, 'd') == 'sbc'


# def test_get_path():
#   graph = get_sample_graph()
#   parents = bfs_path(graph, 's')
#   print(get_path(parents, 'd'))
#   print(parents)
#   #assert get_path(parents, 'd') == 'sbc'

# test_get_path()
