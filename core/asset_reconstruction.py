import networkx as nx

G = nx.read_gpickle("../asset_graph.gpickle")
clusters = list(nx.connected_components(G.to_undirected()))

for i, cluster in enumerate(clusters):
    fragments = [n for n in cluster if G.nodes[n].get("type")=="asset_fragment"]
    vendors = [n for n in cluster if G.nodes[n].get("type")=="vendor"]
    locations = [n for n in cluster if G.nodes[n].get("type")=="location"]
    print("Cluster", i+1)
    print("Fragments:", fragments)
    print("Vendors:", vendors)
    print("Locations:", locations)
    print()
