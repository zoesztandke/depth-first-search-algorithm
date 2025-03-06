from typing import Dict, Set, Union

def dfs(G: Dict[Union[int, str], Set[Union[int, str]]]):
    """
    Depth First Search
    :param G: a graph G
    :return: none
    """
    visited = {node: False for node in G} # initialise boolean array to keep track of visited nodes

    S = [] # stack to keep track of nodes to visit

    for v in G: # for every vertex in G
        if not visited[v]: # if the vertex has not been visited
            dfs_from_vertex(G, v, visited, S) # call dfs from that vertex

def dfs_from_vertex(G: Dict[Union[int, str], Set[Union[int, str]]], v: Union[int, str], visited: Dict[Union[int, str], bool], S: list):
   """
   calls depth first search from the vertex v
   :param G: a graph G
   :param v: the vertex v from which to start the search
   :param visited: a list of states for the vertices
   :param S: stack to keep track of nodes to visit
   :return: none
   """
   S.append(v) # add the vertex to the stack

   while not S.isEmpty(): # while the stack is not empty
       u = S.pop() # remove top vertex from stack
       if not visited[u]: # if the vertex has not been visited
           visited[u] = True # mark the vertex as visited
           for w in G[u]: # for every vertex w adjacent to u
               if not visited[w]: # if the vertex has not been visited
                   S.append(w) # add the vertex to the stack