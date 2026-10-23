import Adress
from Other import OtherFunctions
import os
import snap
from ExtensionDir import Functions

# Nc(u,c(v))=size intersect (n(u) , v(c(v)))  /  size (n(u)  or V(c(v)))


def ExtensionCore(folderRes,folderDes):

    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress +"DataSets\\krogan2006_core.txt", 0, 1)
    # snap.DelDegKNodes(Graph, 1, 1)
    folder=Adress.adress+folderDes
    OtherFunctions.DeleteDirectory(folder)

    cores = os.listdir(Adress.adress+folderRes)

    for core in cores:
        setNodes=set() # node of core  V(c(v))
        name=Adress.adress+ folderRes+"\\" + core
        with open(name, "r")as f:
            for line in enumerate(f):
                for i in line[1].split():
                    setNodes.add(int(i))

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
            if (len(intersect)/len(setNodes)) >0.2:
                setNodes.add(nodeU)
                # with open(name, "a")as f:
                #     print(core)
                #     print("yesssss")
                #     f.write(str(node)+"\n")



        name = Adress.adress + folderDes + "\\" + core
        with open(name, "w")as f:
            for node in setNodes:
                f.write(str(node)+"\n")


# ExtensionCode("DetectClusters")
