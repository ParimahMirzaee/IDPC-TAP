import snap
import function
import function2


# ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
Graph = snap.LoadEdgeListStr(snap.PUNGraph, "dip_output_protein_name.txt", 0, 1)

# unclusterNodes=function2.getNodes(Graph)
# unclusterNodes=Graph.Nodes()
clusterNodes=set()
bonacichNode=function2.selectSeedByBonacich(Graph,clusterNodes)
num=0
evaluateNodes=set()
while(clusterNodes!=snap.CntNonZNodes(Graph)):
    G1 = snap.TUNGraph.New()
    G1.AddNode(bonacichNode)
    neighborNum=0
    baseClusterCoefficient=0
    print(bonacichNode)
    lastBaseClusterCoefficient=0
    while True:
        clusterNodes.add(bonacichNode)
        neighborNum = neighborNum + 1
        NodeVec=function.xThNeighbor(Graph,bonacichNode,neighborNum)
        addedNode = False
        if NodeVec.Len()==0:
            break
        for neighbor in NodeVec:
            G1.AddNode(neighbor)

            # if neighborNum==1:
            #     for all in G1.Nodes():
            #         if (function.isEdgeInGraph(all.GetId(), neighbor, Graph)):
            #             G1.AddEdge(all.GetId(), neighbor)
            #             clusterNodes.add(all.GetId())
            #         # if (function.isEdgeInGraph("%d %d " % (all.GetId(), neighbor))):
            #         #     G1.AddEdge(all.GetId(), neighbor)
            #         # elif (function.isEdgeInGraph("%d %d " % (neighbor, all.GetId()))):
            #         #     G1.AddEdge(neighbor, all.GetId())
            #     baseClusterCoefficient=function.clusterCoefficient(G1)
            #     addedNode = True
            # else:
            result=function.addEdgeOfAddedNode(neighbor, G1, baseClusterCoefficient,Graph,clusterNodes)
            G1=result[0]
            baseClusterCoefficient=result[1]
            notAddNode=result[2]
            clusterNodes=result[3]

        print(neighborNum)
        print(baseClusterCoefficient)

        if(neighborNum!=1 and baseClusterCoefficient-lastBaseClusterCoefficient<=0.01):
        # if(baseClusterCoefficient-lastBaseClusterCoefficient<0.05):
            break
        lastBaseClusterCoefficient = baseClusterCoefficient
    print("b=%f"%baseClusterCoefficient)
    evaluateNodes.add(bonacichNode)
    num=num+1
    print("num=%d"%num)
    snap.SaveEdgeList(G1,"%d.txt"%bonacichNode)
    bonacichNode = function2.selectSeedByBonacich(Graph,clusterNodes)
    numNotExtend = 0
    if(bonacichNode==-1):
    #     while(bonacichNode==-1):
    #         numNotExtend+=1
    #         # clusterNodes.append(bonacichNode)
    #         bonacichNode = function2.selectSeedByBonacich(Graph,clusterNodes)
    #         if(numNotExtend>10):
    #             break
    # if (numNotExtend > 10):
        break
# snap.SaveEdgeList(Graph,"RemainGraph.txt"
function2.ConvertToName(evaluateNodes)
print(len(clusterNodes))
print(num-1)
