from Extension import  Functions
import snap
def Extension(Graph,cluster,weight):
    clusterCopy = set()
    allNeighbir=set()
    while True:
        allFirstNeighbors=set()
        #get first neighbor of nodes of cluster
        for node in cluster:
            for n in cluster:
                clusterCopy.add(n)

            firstNeighborNode = snap.TIntV()
            snap.GetNodesAtHop(Graph, node, 1, firstNeighborNode, False)
            for a in firstNeighborNode:
                allNeighbir.add(a)


        firstNeighborNode = Functions.order2(allNeighbir, weight)
        sum = 0
        for key, value in firstNeighborNode.items():
            sum+=value
        if len(firstNeighborNode)!=0:
            mean = sum / len(firstNeighborNode)
        else:mean=sum

        for fn in firstNeighborNode:
            # allFirstNeighbors.add(fn)
            s=firstNeighborNode[fn]
            if fn not in cluster and firstNeighborNode[fn]>=mean:
                clusterCopy.add(fn)
                dim=diameter(Graph,clusterCopy)
                if dim<=3:
                    allFirstNeighbors.add(fn)

                clusterCopy.remove(fn)


        if len(allFirstNeighbors)>0:
            orderCondidateNodes=Functions.order2(allFirstNeighbors,weight)
            a=next(iter(orderCondidateNodes))
            cluster.add(a)
        else:
            return cluster






def diameter(Graph,cluster):
    NIdV = snap.TIntV()
    for node in cluster:
        NIdV.Add(node)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    return snap.GetBfsFullDiam(SubGraph, len(cluster), False)


