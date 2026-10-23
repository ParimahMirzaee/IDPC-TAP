import snap
def xThNeighbor(graph,id,x):
    NodeVec = snap.TIntV()
    snap.GetNodesAtHop(graph,id,x, NodeVec, False)
    # for item in NodeVec:
    #     print(item)
    return  NodeVec

def isEdgeInGraph(node1,node2,Graph):
    # with open('dip_output_protein_name.txt') as f:
    #     if x in f.read():
    #         return True
    #     else:
    #         return False

    if(Graph.IsEdge(node1,node2)):
        return True
    else:
        return False


def addEdgeOfAddedNode(neighbor,G1,baseClusterCoefficient,Graph,clusterNodes):
    for all in G1.Nodes():
        if(isEdgeInGraph(all.GetId(),neighbor,Graph)):
            G1.AddEdge(all.GetId(),neighbor)


    newCC=clusterCoefficient(G1)
    if(newCC>=baseClusterCoefficient):
        # v = snap.TIntV()
        # v.Add(neighbor)
        baseClusterCoefficient=newCC
        notAddNode=False
        # snap.DelNodes(Graph, v)
        clusterNodes.add(neighbor)
    else:
        notAddNode=True
        G1.DelNode(neighbor)

    return G1,baseClusterCoefficient,notAddNode,clusterNodes

def selectSeedByBonacichForExtension(Graph,NodeVec,bonacichNode):
    degreeNodes = function.allDegreeNodesGraph(Graph)
    # highDegreeNodeId = largestDegrees(degreeNodes,clusterNodes)
    highDegreeNodeId=[None] * len(NodeVec)
    i=0
    maxHigh=0
    for neighbor in NodeVec:
        highDegreeNodeId[i]=neighbor
        if(function.getDegreeSpecificNode(neighbor,degreeNodes)>maxHigh):
            maxHigh=neighbor
        i+=1

    # همسایه های نودهای با درجه بالا را بدست می‌آوریم.
    bonacichNodes = dict()
    for NI in Graph.Nodes():
        a=NI.GetId()
        if (NI.GetId() in highDegreeNodeId):
            i = 0
            for Id in NI.GetOutEdges():
                degree = function.getDegreeSpecificNode(Id, degreeNodes)
                high=function.getDegreeSpecificNode(maxHigh,degreeNodes)
                if(degree>high/2):
                    i=i+1
                bonacichNodes[NI.GetId()] = i
    max=nlargest(len(bonacichNodes),bonacichNodes,key=bonacichNodes.get)
    return max


# **************************************************************************************************
def deleteThreeLine(name):
    f = open(name, 'r')
    linelist = f.readlines()
    f.close
    # Re-open file here
    f2 = open(name, 'w')
    f2.writelines(linelist[3: ])
    f2.close()
# ***************************************************************************************

# برگرداندن درجه نودهای گراف
def degreeNodesList(Graph,list):
    InDegV = snap.TIntPrV()
    snap.GetNodeInDegV(Graph, InDegV)
    dictDegreeDip = {}
    for item in InDegV:
        if item.GetVal1() in list:
            dictDegreeDip[item.GetVal1()] = item.GetVal2()
    dictDegreeDip = {k: v for k, v in sorted(dictDegreeDip.items(), key=lambda x: x[1], reverse=True)}
    return dictDegreeDip


# برگرداندن cc
def ClusterCoefficientsList(Graph,beforeNode,list):
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(Graph, NIdCCfH)
    dictcc = {}
    for item in NIdCCfH:
        if item in list and item!= beforeNode:
            dictcc[item] = NIdCCfH[item]
    dictCCDip = {k: v for k, v in sorted(dictcc.items(), key=lambda x: x[1], reverse=True)}
    return dictCCDip


def getNodesOfClustersOfFolder(folder):
    import os
    import Adress
    nodes = set()
    clusters = os.listdir(Adress.adress + folder)
    for cluter in clusters:
        name = Adress.adress+folder+"\\"+cluter
        with open(name, "r") as file:
            for line in file:
                nodes.add(int(line[:-1]))

    return nodes


def order(vec,weight,beforeNode):
    Dict=dict()
    for i in vec:
        if i!= beforeNode:
            Dict[i]=weight[i]

    data_sorted = {k: v for k, v in sorted(Dict.items(), key=lambda x: x[1], reverse=True)}
    return data_sorted


def order2(vec,weight):
    Dict=dict()
    for i in vec:
        if i in weight:
            Dict[i]=weight[i]

    data_sorted = {k: v for k, v in sorted(Dict.items(), key=lambda x: x[1], reverse=True)}
    return data_sorted