import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from itertools import cycle

grade_dict = {"1A": "red", "1B": "red", "2A": "orange", "2B": "orange", "3A": "gray", "3B": "gray", "4A": "cyan", "4B": "cyan", "5A": "blue", "5B": "blue", "Teachers": "black"}
grade_dict_more = {"1A": "firebrick", "1B": "red", "2A": "orange", "2B": "sandybrown", "3A": "slategray", "3B": "gray", "4A": "darkturquoise", "4B": "cyan", "5A": "cornflowerblue", "5B": "blue", "Teachers": "black"}


# Assign colors to each community
def assign_colors_to_communities(G, communities):
    pos = nx.spring_layout(G)  # Layout for visualization
    color_cycle = cycle(plt.cm.tab10.colors)  # Color palette
    node_colors = {}

    for i, community in enumerate(communities[0]):  # Consider the first level of communities
        color = next(color_cycle)
        for node in community:
            node_colors[node] = color

    return pos, node_colors

# Draw the graph
def draw_graph_with_communities(G, pos, node_colors):
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()), cmap=plt.cm.tab10, node_size=100)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
    plt.title("Communities Visualization")
    plt.show()

def draw_graph_per_community(G, pos, node_colors, communities):
    fig, axes = plt.subplots(1, len(communities), figsize=(7*len(communities), 8))
    print(len(communities))
    if len(communities) == 1:
        axes = [axes]  # Ensure axes is iterable

    for ax, community in zip(axes, communities):
        subgraph = G.subgraph(community)
        nx.draw(subgraph, pos, ax=ax, node_color=node_colors, with_labels=True, node_size=100, edge_color='gray')
        ax.set_title(f"Community {communities.index(community) + 1}")

    plt.show()