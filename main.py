
import csv
from tokenize import group
from pyvis.network import Network
import networkx as nx
import os

if __name__ == "__main__":
    files = os.listdir("data")
    nx_graph = Network()
    
    people=[]
    types=[]
    for file in files:
        if file.endswith(".csv") and not file.startswith("Example"):
            with open('./data/'+file, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    if row[0] not in people:
                        people.append(row[0])
                    if row[1] not in people:
                        people.append(row[1])
                    if row[2] not in types:
                        types.append(row[2])
                    
    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#000000', '#FFFFFF']                    

    for file in files:
        if file.endswith(".csv") and not file.startswith("Example"):
            with open('./data/'+file, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                    nx_graph.add_node(row[0], title=row[0], group=people.index(row[0]))
                    nx_graph.add_node(row[1], title=row[1], group=people.index(row[1]))
                    nx_graph.add_edge(row[0], row[1], weight=1, title=row[2], color=colors[types.index(row[2])], label=row[2])
    
    
    nx_graph.show('./docs/index.html', notebook=False)