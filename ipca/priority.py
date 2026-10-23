import snap


def cc(Graph):
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(Graph, NIdCCfH)
    return NIdCCfH


# d :thereshold for diameter and short path
# T : threshold for In
def testNodes(Graph,cluster,neighbors,T,d):
    dictPrior=dict()
    NIdCCfH=cc(Graph)
    for vertex in neighbors:
        #use inv
        intersect = 0
        for node in cluster:
            if (Graph.IsEdge(node, vertex)):
                intersect+=1
        n=len(cluster)
        inv=intersect/n
        if inv>=T:
            dictPrior[vertex]=inv


        #use cc
        # a=NIdCCfH(item)
        # if NIdCCfH(vertex) >= T:
        #     dictPrior[vertex]=NIdCCfH(vertex)

    #شرط خاتمه : اگر هیچ همسایه ای نداشته باشد
    if len(dictPrior)==0:
        return False
    r = dict(sorted(dictPrior.items(), key=lambda x:x[1], reverse=True))
    l = list(r.keys())
    for a in l :
        cluster.add(a)
        # if shortPath(Graph,cluster)<=d:
        if shortPath(Graph,cluster)<=d or diameter(Graph,cluster)<=d:
            return cluster
        else:
            cluster.remove(a)

    return False





def diameter(Graph,cluster):
    NIdV = snap.TIntV()
    for node in cluster:
        NIdV.Add(node)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    return snap.GetBfsFullDiam(SubGraph, len(cluster), False)


def shortPath(Graph,cluster):
    NIdV = snap.TIntV()
    for node in cluster:
        NIdV.Add(node)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    result = snap.GetBfsEffDiamAll(SubGraph, 10, False)
    return result[3]
