#  File: TopoSort.py

#  Description: Test if the given Graph does not contain a cycle
                # Then do a topological sort on that Graph
                #Finally, print the vertices on a given level in alphabetical order

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 04/ 17/ 2023

#  Date Last Modified: 04/ 21/ 2023
import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))
  
  def peek(self):
    return self.queue[0]


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  def get_adj_vertices (self, v):
    veticies = len(self.Vertices)
    list = []
    for i in range (veticies):
        if self.adjMat[v][i] > 0:
            list.append(self.Vertices[i])
    return list
  
  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1
  
  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle(self):
      dict = {}
      nVert = len(self.Vertices)
      for i in range(nVert):
          self.Vertices[i].visited = False
          dict[i] = 'unchecked'
      check = False
      for vertex in range(nVert):
          if dict[vertex] == 'unchecked':
              check = self.has_cycle_helper(vertex, dict)
          if dict[vertex] == 'checked':
             check = True
          if check:
              break
      #print(dict)
  
      return check

  def has_cycle_helper(self, vertex, dict):
    adjacent = self.get_adj_vertices(vertex)
    dict[vertex] = 'checked'
    for i in adjacent:
        if dict[self.Vertices.index(i)] == 'checked':
            return True
        if dict[self.Vertices.index(i)] == 'unchecked':
            self.has_cycle_helper(self.Vertices.index(i), dict)
    dict[vertex] = 'done'

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort(self):
    queue = Queue()
    nVert = len(self.Vertices)
    dict = {}
    for vertex in range(nVert):
        count = 0
        for n in range(nVert):
            if self.adjMat[n][vertex] > 0:
                count += 1
        dict[self.Vertices[vertex]] = count

    while len(dict) > 0:
        list = []
        for key in dict:
            if dict[key] == 0:
                list.append(key)
        list_queue = []
        for key in list:
            idx = self.Vertices.index(key)
            for vertex in range(nVert):
                    if self.adjMat[idx][vertex] > 0:
                        dict[self.Vertices[vertex]] -= 1
            dict.pop(key)
            list_queue.append(key.label)
        list_queue.sort()
        for i in list_queue:
            queue.enqueue(i)
    result = []

    while not(queue.is_empty()):
        add_queue = queue.dequeue()
        result.append(add_queue)

    return result

def main():
  # create the Graph object
  theGraph = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)
  #print(n)

  # read the vertices to the list of Vertices
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    theGraph.add_vertex (line)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  n_2 = int (line)
  #print(n_2)

  # read each edge and place it in the adjacency matrix
  for i in range (n_2):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    for vertice in theGraph.Vertices:
        if vertice.label == line[0]:
            start = theGraph.Vertices.index(vertice)
        if vertice.label == line[1]:
            finish = theGraph.Vertices.index(vertice)
    theGraph.add_directed_edge (start, finish, 1)

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)   

if __name__ == "__main__":
  main()
