# frc_lib/undirected_frc.py

import numpy as np
import networkx as nx

class FormanRicci:
    def __init__(self, G):
        self.G = G.copy()

    def compute_ricci_curvature(self):
        """
        Compute the Forman-Ricci curvature for all edges and nodes in an undirected graph G.
        """
        if self.G.is_directed():
            raise ValueError("The graph must be undirected.")

        # Initialize a dictionary to store the curvature values
        curvature = {}

        # Iterate over all edges in the graph
        for u, v in self.G.edges():
            # Get the edge weight (default to 1 if not provided)
            w_e = self.G[u][v].get('weight', 1)

            # Get the node weights (default to 1 if not provided)
            w_u = self.G.nodes[u].get('weight', 1)
            w_v = self.G.nodes[v].get('weight', 1)

            # Initialize the summation terms
            sum_u = 0
            sum_v = 0

            # Sum over the edges adjacent to node u
            for _, u_neigh in self.G.edges(u):
                if u_neigh != v:
                    w_u_neigh = self.G[u][u_neigh].get('weight', 1)
                    sum_u += w_u / np.sqrt(w_e * w_u_neigh)

            # Sum over the edges adjacent to node v
            for _, v_neigh in self.G.edges(v):
                if v_neigh != u:
                    w_v_neigh = self.G[v][v_neigh].get('weight', 1)
                    sum_v += w_v / np.sqrt(w_e * w_v_neigh)

            # Calculate the Forman-Ricci curvature for the edge (u, v)
            F_e = w_e * (w_u / w_e + w_v / w_e - sum_u - sum_v)

            # Store the curvature value
            curvature[(u, v)] = F_e
            self.G[u][v]['formanCurvature'] = F_e

        # Calculate average Forman-Ricci curvature for each node
        for n in self.G.nodes():
            fcsum = 0
            if self.G.degree(n) != 0:
                for nbr in self.G.neighbors(n):
                    if 'formanCurvature' in self.G[n][nbr]:
                        fcsum += self.G[n][nbr]['formanCurvature']
                self.G.nodes[n]['formanCurvature'] = fcsum / self.G.degree(n)
            else:
                self.G.nodes[n]['formanCurvature'] = 0

        print("Forman curvature computation done.")
        return self.G
