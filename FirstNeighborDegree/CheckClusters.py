import snap
import Adress
import os
from shutil import copyfile
from PickleData import convertToName
from Evaluate import Evaluate
from Other import OtherFunctions
from SelectSeed import SeedCoefficient

resFolder= Adress.adress + "FirstNeighborDegree\\NewDetectClusters\\"
desFolder=Adress.adress + "FirstNeighborDegree\\cluster0.5\\"
Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)


# extension clusters with 0=<cc<threshold with their first neighbors
def extension(Graph,clusterNames,threshold):
    # clusterNames : list of cluster with 0=<cc<threshold
    for cluster in clusterNames:
        clusterNodes=set()
        name = resFolder + str(cluster)
        NIdV = snap.TIntV()
        with open(name, "r") as file:
            for line in file:
                NIdV.Add(int(line[:-1]))
                clusterNodes.add(int(line[:-1]))
        SubGraph = snap.GetSubGraph(Graph, NIdV)

        NIdV2=NIdV
        # coefficient
        for node in NIdV2:
            NodeVec = snap.TIntV()
            snap.GetNodesAtHop(Graph, node, 1, NodeVec, False)
            firstNeighborVec = SeedCoefficient.largestDegreesWithBonacich(Graph, 0, NodeVec)
            CfVec = snap.TFltPrV()
            Cf = snap.GetClustCf(SubGraph, CfVec, -1)
            for neighbor in firstNeighborVec:
                if neighbor not in NIdV:
                    NIdV.Add(neighbor)
                    clusterNodes.add(neighbor)
                    SubGraph = snap.GetSubGraph(Graph, NIdV)
                    CfVec2 = snap.TFltPrV()
                    Cf2 = snap.GetClustCf(SubGraph, CfVec2, -1)

                    if Cf2[0]<Cf[0]:
                        clusterNodes.remove(neighbor)
                        NIdV = snap.TIntV()
                        for i in clusterNodes:
                            NIdV.Add(i)
                        SubGraph = snap.GetSubGraph(Graph, NIdV)

        CfVec3 = snap.TFltPrV()
        Cf3 = snap.GetClustCf(SubGraph, CfVec3, -1)
        if Cf3[0]>threshold:
            name = desFolder + str(cluster)
            with open(name, "w") as myfile:
                for node in clusterNodes:
                    myfile.write(str(node) + "\n")



def selectClusters(threshold):
    bonacichNodes = os.listdir(resFolder)
    notGoodCluster=list()
    for i in bonacichNodes:
        name = resFolder + str(i)
        NIdV = snap.TIntV()
        with open(name, "r") as file:
            for line in file:
                NIdV.Add(int(line[:-1]))

        SubGraph = snap.GetSubGraph(Graph, NIdV)


        # coefficient
        CfVec = snap.TFltPrV()
        Cf = snap.GetClustCf(SubGraph, CfVec, -1)
        # print("Average Clustering Coefficient: " + str(Cf[0]))
        if Cf[0]>=threshold:
            dst=desFolder + str(i)
            copyfile(name, dst)

        #*************************************** اضافه کردن کلاستر هایی که کمتر هستند*****************************************
    #     elif Cf[0]>=0 and Cf[0]<threshold:
    #         notGoodCluster.append(i)
    #
    # extension(Graph,notGoodCluster,threshold)



# نوشتن نودهایی ک کلاستر شده ه اند در داخل یک فایل
def allClusterdNode():
    bonacichNodes = os.listdir(desFolder)
    nodes=set()
    for i in bonacichNodes:
        name =desFolder+ str(i)
        with open(name, "r") as file:
            for line in file:
                nodes.add(int(line[:-1]))
    name = desFolder+"allNodes.txt"
    fileOut=open(name,'w')
    for i in nodes:
        fileOut.write(str(i)+"\n")
    fileOut.close()



#اضافه کردن نودهایی که کلاستر نشده اند به کلاستر ها
def addGoodNodesToClusters():
    clusteredNodes=set()
    name = desFolder+"allNodes.txt"
    with open(name, "r") as file:
        for line in file:
            clusteredNodes.add(int(line[:-1]))

    detectClusters = os.listdir(desFolder)
    print(len(clusteredNodes))
    i=0
    for NI in Graph.Nodes():
        if NI.GetId() not in clusteredNodes:
            maxCoefficient=0
            maxCluster="#"
            for cluster in detectClusters:
                if cluster!="allNodes.txt":
                    name = desFolder+ str(cluster)
                    NIdV = snap.TIntV()
                    with open(name, "r") as file:
                        for line in file:
                            NIdV.Add(int(line[:-1]))
                    NIdV.Add(NI.GetId())
                    SubGraph = snap.GetSubGraph(Graph, NIdV)
                    CfVec = snap.TFltPrV()
                    Cf = snap.GetClustCf(SubGraph, CfVec, -1)
                    if Cf[0]>maxCoefficient:
                        maxCluster=cluster

            if maxCluster!="#":
                name = desFolder + str(maxCluster)
                with open(name, "a") as myfile:
                    myfile.write(str(NI.GetId())+"\n")
                clusteredNodes.add(NI.GetId())
            i+=1
            print(i)





# baseCode
# threshold=0.7
# selectClusters(threshold)
# allClusterdNode()
# addGoodNodesToClusters()
os.remove(desFolder+"\\"+"allNodes.txt")
convertToName.ConvertToName(desFolder)
Evaluate.Evaluate()

