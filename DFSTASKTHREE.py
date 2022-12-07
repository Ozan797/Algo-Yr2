# Python program to print all paths from a source to destination.

from collections import defaultdict
import numpy as np
import pandas as pd
data = pd.read_excel('London Underground data2.xlsx')


# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
            print(path)
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


def unique_st():
    stations = []

    for i in data['From']:
        stations.append(i.strip())
    return list(np.unique(stations))


unique_stations = unique_st()
unique_stations_dict = {}

for ids, station in enumerate(unique_stations):
    unique_stations_dict[station] = ids

stations_dict = {}

for ids, row in enumerate(data.values):
    if str(row[3]) == 'nan':
        continue
    if [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(row[2]).strip()]] in stations_dict.values():
        continue
    if [unique_stations_dict[str(row[2]).strip()], unique_stations_dict[str(row[1]).strip()]] in stations_dict.values():
        continue
    stations_dict[ids] = [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(row[2]).strip()]]

# Create a graph given in the above diagram
g = Graph(270)
for i in stations_dict.keys():
    g.addEdge(stations_dict[i][0], stations_dict[i][1])

s = 2
d = 56
print("Following are all different paths from % d to % d :" % (s, d))
g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav
