import snap
def Density(Graph):
    edges= snap.CntUniqUndirEdges(Graph)
    nodes=snap.CntNonZNodes(Graph)

    if nodes<2:
        return 0
    else:
        density = 2 * edges / (nodes * (nodes-1))
        return density
