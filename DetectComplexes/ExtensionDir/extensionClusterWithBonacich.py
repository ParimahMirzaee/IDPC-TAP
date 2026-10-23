import snap
import function
import function2


# ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension با bonacich
Graph = snap.LoadEdgeListStr(snap.PUNGraph, "dip_output_protein_name.txt", 0, 1)
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

        max=function2.selectSeedByBonacichForExtension(Graph,NodeVec,bonacichNode)

        for neighbor in max:
            G1.AddNode(neighbor)
            result=function.addEdgeOfAddedNode(neighbor, G1, baseClusterCoefficient,Graph,clusterNodes)
            G1=result[0]
            baseClusterCoefficient=result[1]
            notAddNode=result[2]
            clusterNodes=result[3]

        print(neighborNum)
        print(baseClusterCoefficient)

        if(neighborNum!=1 and baseClusterCoefficient-lastBaseClusterCoefficient<=0.01):
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
        break
function2.ConvertToName(evaluateNodes)
print(len(clusterNodes))
print(num-1)
