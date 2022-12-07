# Kruskal's algorithm in Python
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
import Task_1
data = pd.read_excel('London Underground data.xlsx')

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        # for u, v, weight in result:
            # print(f'{get_key(u)} - {get_key(v)} {weight}')
        return result


def get_key(val):
    for key, value in unique_stations_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


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
    if [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(row[2]).strip()], int(row[3])] in stations_dict.values():
        continue
    if [unique_stations_dict[str(row[2]).strip()], unique_stations_dict[str(row[1]).strip()], int(row[3])] in stations_dict.values():
        continue
    stations_dict[ids] = [unique_stations_dict[str(row[1]).strip()], unique_stations_dict[str(row[2]).strip()], int(row[3])]

g = Graph(270)

for i in stations_dict.keys():
    g.add_edge(stations_dict[i][0], stations_dict[i][1], stations_dict[i][2])

for_dijkstra = g.kruskal_algo()

graph = nx.Graph()
graph.add_weighted_edges_from(for_dijkstra)

departing_station = "Piccadilly Circus"
arriving_station = "Paddington"
path = nx.dijkstra_path(graph, unique_stations_dict[departing_station], unique_stations_dict[arriving_station])
path_names = []
for i in path:
    path_names.append(get_key(i))
print(path_names, nx.dijkstra_path_length(graph, unique_stations_dict[departing_station], unique_stations_dict[arriving_station], weight='weight')) # normalden 1 dakika az buluyo

Task_1.histogram_1b(for_dijkstra)
# print(len(for_dijkstra))
# graph = nx.Graph()
# start = time.time()
# graph.add_weighted_edges_from(for_dijkstra)
# all_weighted_paths = []
# histogram_list = []
# for i in for_dijkstra:
#     for j in for_dijkstra:
#         x = nx.dijkstra_path(graph, i[0], j[1])  # Call the path for variable of 'x'.
#         y = nx.dijkstra_path_length(graph, i[0], j[1])  # Call the distance for variable of 'y'.
#         if [x, y] not in all_weighted_paths:  # If the paths and the distances are not in the 'all_weighted_path' list, it will append them into it.
#             all_weighted_paths.append([x, y])
# for i in all_weighted_paths:  # Fetching only all the distances, in order to plot a histogram.
#     histogram_list.append(i[1])
#
# plt.hist(histogram_list, bins=range(0, 111, 1), color='black', edgecolor='white')  # Creating the display for the histogram.
# plt.xticks(range(0, 111, 1), fontsize=8, color="#572681")
# plt.title('What the title supposed to be?')
# plt.xlabel("Minutes")  # x axis
# plt.ylabel("Journey Frequency")  # y axis
# print('Time passed during the process: ', time.time()-start)
# print(len(histogram_list))
# plt.show()
