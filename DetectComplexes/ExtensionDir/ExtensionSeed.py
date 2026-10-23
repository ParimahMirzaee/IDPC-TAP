import Adress
from Other import OtherFunctions
import os
import snap
from Extension import Functions

# Nc(u,c(v))=size intersect (n(u) , v(c(v)))  /  size (n(u)  or V(c(v)))


def ExtensionSeed(setNodes,folderDes,nn,ss):
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress +"DataSets\\krogan2006_core.txt", 0, 1)
    # snap.DelDegKNodes(Graph, 1, 1)
    # folder=Adress.adress+folderDes
    # OtherFunctions.DeleteDirectory(folder)


    # setNodes=set() # node of core  V(c(v))

    setFirstNeighbors=set()  # first neighbor of all nodes in core (candidate nodes for select u )
    for node in setNodes:
        vec=Functions.xThNeighbor(Graph,node,1)
        for n in vec:
            if n not in setNodes:
                setFirstNeighbors.add(n)

    for nodeU in setFirstNeighbors:
        setNeighborCandidateNodeU=set() # first neighbor of candidatwe node u  n(u)
        Nu=Functions.xThNeighbor(Graph,nodeU,1)
        for n in Nu:
            setNeighborCandidateNodeU.add(n)
        intersect = list(set(setNodes) & set(setNeighborCandidateNodeU))
        # print(len(intersect)/len(li))
        # if (len(intersect)/len(Nu)) >= 0.64:
        # if (len(intersect)/len(setNeighborCandidateNodeU)) >= 0.64:
        if (len(intersect)/len(setNodes)) >0.4:
            setNodes.add(nodeU)
            ExtensionSeed(setNodes, "ExtensionCores",nn+1,-1)

    if nn==0:
        # for e in setNodes:
        name = Adress.adress + folderDes + "\\" +str(ss)+".txt"
        with open(name, "w")as f:
            for node in setNodes:
                f.write(str(node)+"\n")
            # break