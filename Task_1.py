# importing the libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

data = pd.read_excel('London Underground data.xlsx')  # Getting the datas from provided excel sheet


def all_stations_with_times():  # Calling all the immediate stations with times into list
    stations = []
    for row in data.values:
        if str(row[3]) != 'nan':  # Ignoring the 'nan' strings
            stations.append([row[1].strip(), row[2].strip(), int(row[3])])  # Added strip() method to station names in order to fix the error of spaces of provided data
    return stations


def graph(calling_st):  # Creating the graph for Dijkstra
    gr = nx.Graph()
    gr.add_weighted_edges_from(calling_st)  # Getting the nodes and edges with their weights
    return gr


def dijkstra_path(gr, departing_st, arriving_st):
    path = nx.dijkstra_path(gr, departing_st, arriving_st)  # Using the 'Dijkstra' in order to find the shortest path
    return path


def dijkstra_distance(gr, departing_st, arriving_st):
    distance = nx.dijkstra_path_length(gr, departing_st, arriving_st, weight='weight')  # Added the weight to find the sum of the taken times between given stations to get the total distance
    return distance


# departing_station = str(input("Please provide 'Destination' point of your journey?\n")).title().strip() # Taking input from the customer as a start point
# arriving_station = str(input("Please provide 'Arriving' point of your journey?\n")).title().strip() # Taking input from the customer as end point

# departing_station = "Piccadilly Circus".title()
# arriving_station = "Paddington".title()

create_graph = graph(all_stations_with_times())
# shortest_path = dijkstra_path(create_graph, departing_station, arriving_station)
# shortest_distance = dijkstra_distance(create_graph, departing_station, arriving_station)
# print(f'Shortest list of stations the customer will travel: {shortest_path}\n\nTotal taken time for journey between {departing_station} - {arriving_station}: {shortest_distance} minutes.')  # Displayed total taken times between the stations.


# Creating the histogram with all the quickest possible journeys (Depends on time).
def histogram_1b(stations_times):
    gra = graph(stations_times)
    all_weighted_paths = []  # Fetching all the possible paths with their distances.
    histogram_list = []  # Fetching only all the distances, in order to plot a histogram.
    start = time.time()

    for i in stations_times:
        for j in stations_times:
            x = dijkstra_path(gra, i[0], j[1])  # Call the path for variable of 'x'.
            y = dijkstra_distance(gra, i[0], j[1])  # Call the distance for variable of 'y'.
            # If the paths and the distances are not in the 'all_weighted_path' list, it will append them into it.
            if [x, y] not in all_weighted_paths:  # If the paths and the distances are not in the 'all_weighted_path' list, it will append them into it.
                all_weighted_paths.append([x, y])
    # z = list(set(all_weighted_paths))
    # print(type(all_weighted_paths), len(all_weighted_paths))
    for i in all_weighted_paths:  # Fetching only all the distances, in order to plot a histogram.
        histogram_list.append(i[1])

    print('\nNumber of all possible journeys:', len(histogram_list))  # Displaying the length of the 'histogram_list'.

    plt.hist(histogram_list, bins=range(0, 111, 1), color='black', align='right', edgecolor='white')  # Creating the display for the histogram.
    plt.xticks(range(0, 111, 1), fontsize=8, color="#572681")
    plt.xlabel("Minutes")  # x axis
    plt.ylabel("Journey Frequency")  # y axis
    print('\nTotal time taken while histogram being created : ', (time.time() - start))

    plt.show()


# histogram_1b(all_stations_with_times())
