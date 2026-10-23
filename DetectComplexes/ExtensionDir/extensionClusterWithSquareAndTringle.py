import snap
from Merge import Merge
from SelectSeed import functionFirstSeed

from  Extension import  Functions
from Criterion import ClusterCoefficient , Density
from PickleData import convertToName
from SelectNextNode import Function
num=0
clusterNodesSet=set()
numLessThanTwo=0
notCCmorethanZeroList = []
evaluateNodesSet=set()

# ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, "dip_output_protein_name.txt", 0, 1)
Graph = snap.LoadEdgeListStr(snap.PUNGraph, "..\DataSets\DIP_ProteinName.txt", 0, 1)
#بدست آوردن دانه ها
bonacichNodes= functionFirstSeed.selectSeedByBonacichInFirst(Graph, clusterNodesSet)
# bonacichNodes=example2.selectSeed(Graph)
# bonacichNode=function2.selectSeedByBonacich(Graph, clusterNodesSet, None)


#تا زمانی که پروتئین باقی مانده باشد ادامه دارد.
# while(len(clusterNodesSet) != snap.CntNonZNodes(Graph)):
for bonacichNode in bonacichNodes:
    bonacichNode=int(bonacichNode)
# if(bonacichNode not in clusterNodesSet):
    G1 = snap.TUNGraph.New()
    clusterG1=set()
    G1.AddNode(bonacichNode)
    FirstDensity = 0
    baseClusterCoefficient=0
    lastBaseClusterCoefficient=0
    clusterG1.add(bonacichNode)
    firstNeighborVec=Functions.xThNeighbor(Graph, bonacichNode, 1)
    if firstNeighborVec.Len()==0:
        continue
    # یک for برای همسایه‌های اول
    for firstNeighbor in firstNeighborVec:
        if(firstNeighbor!= bonacichNode):
            addedSecondNeighbor=False


            if firstNeighbor not in clusterG1:
                G1.AddNode(firstNeighbor)
                # clusterG1.add(firstNeighbor)
                # clusterNodes.add(firstNeighbor)



            sub=0 # اشتراک
            #تمام همسایه های اول اضافه می‌شوند و چک می شود ک آیا با نودهای دیگر که درون گراف هستند یا درواقع با نودهای همسایه اول دیگر رابطه دارند یا خیر؟
            for eachNode in G1.Nodes():
                if (Functions.isEdgeInGraph(eachNode.GetId(), firstNeighbor, Graph)):
                    G1.AddEdge(eachNode.GetId(), firstNeighbor)
                    sub+=1


            # if(ClusterCoefficient.clusterCoefficient(G1)>=baseClusterCoefficient):
            #    clusterG1.add(firstNeighbor)
            #     # baseClusterCoefficient=function.clusterCoefficient(G1)
            #     # clusterNodes.add(firstNeighbor)
            #     # print("yes")
            # else:
            #     # print("no")
            #     G1.DelNode(firstNeighbor)
            #     continue


            # add first neighbor due to density

            SecondDensity=Density.Density(G1)
            if(SecondDensity>=FirstDensity):
                clusterG1.add(firstNeighbor)
                # baseClusterCoefficient=function.clusterCoefficient(G1)
                # clusterNodes.add(firstNeighbor)
                # print("yes")
            else:
                # print("no")
                G1.DelNode(firstNeighbor)
                continue


            # همسایه اول در صورتی اضافه می شود که closeness آن بیشتر از ۰.۵ شود.
            # count = snap.CntNonZNodes(G1)
            # closeness=sub/count
            # if(closeness>0.5):
            #     clusterG1.add(firstNeighbor)
            #     print("yes")
            #     # clusterNodes.add(firstNeighbor)
            # else:
            #     print("no")
            #     G1.DelNode(firstNeighbor)
            #     continue


            #بدست آوردن همسایه های دوم با عبور از این همسایه اول
            #یا در واقع همسایه های اول همسایه اول مشخص شده
            secondNeighborVec = Functions.xThNeighbor(Graph, firstNeighbor, 1)
            # چک شود ک به جز firstneighbor همسایه دیگری داشته باشد
            if len(secondNeighborVec)!=1:
                #حالا باید طبق bonacich چندتا از نودهارو انتخا کنم
                result=Function.selectSecondNeighborForExtenionWithBonacich(bonacichNode,secondNeighborVec,Graph)
                bonacichNodeFromSecondNeighbor=result[0]
                if bonacichNodeFromSecondNeighbor==-1:
                    continue
                for secondNeighbor in bonacichNodeFromSecondNeighbor:
                    if (secondNeighbor != bonacichNode):
                        if(Functions.isEdgeInGraph(bonacichNode,secondNeighbor,Graph)):
                            #مثلث ببین نود اصلی و همسایه دوم ایجاد شده است
                            addedSecondNeighbor=True
                            if(secondNeighbor==174):
                                d=1
                            if secondNeighbor not in clusterG1:
                                G1.AddNode(secondNeighbor)
                                clusterG1.add(secondNeighbor)
                                # clusterNodes.add(secondNeighbor)
                            for eachNode in G1.Nodes():
                                if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                    G1.AddEdge(eachNode.GetId(), secondNeighbor)


                        #چه مثلث قبلی ایجاد شده بود چ نشده بود باید همسایه سوم را نیز بررسی کنیم.
                        # thirdNeighborVec = function.xThNeighbor(Graph, secondNeighbor, 1)
                        thirdNeighborSelected=result[1][secondNeighbor]
                        thirdNeighbors=Function.selectThirdNeighborWithHighDegree(firstNeighbor,thirdNeighborSelected,Graph)
                        if(thirdNeighbors==-1):
                            continue

                        if len(thirdNeighbors)!=1:
                            for thirdNeighbor in thirdNeighbors:
                                triangle = square = False
                                # if (thirdNeighbor != bonacichNode):
                                if (Functions.isEdgeInGraph(bonacichNode, thirdNeighbor, Graph)):
                                    # مربع ببین نود اصلی و همسایه سوم ایجاد شده است
                                    if thirdNeighbor not in clusterG1:
                                        G1.AddNode(thirdNeighbor)
                                        clusterG1.add(thirdNeighbor)
                                        # clusterNodes.add(thirdNeighbor)
                                    square=True
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), thirdNeighbor)

                                elif (Functions.isEdgeInGraph(firstNeighbor, thirdNeighbor, Graph)):
                                    # مثلث ببین همسایه اول و همسایه سوم ایجاد شده است
                                    if thirdNeighbor not in clusterG1:
                                        G1.AddNode(thirdNeighbor)
                                        clusterG1.add(thirdNeighbor)
                                        # clusterNodes.add(thirdNeighbor)
                                    triangle=True
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), thirdNeighbor)

                                if((triangle or square)  and not addedSecondNeighbor):
                                    if secondNeighbor not in clusterG1:
                                        G1.AddNode(secondNeighbor)
                                        clusterG1.add(secondNeighbor)
                                        # clusterNodes.add(secondNeighbor)
                                    addedSecondNeighbor=True
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), secondNeighbor)

        baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
        SecondDensity = Density.Density(G1)
   #پایان for برای همسایه های اول هر seed



    #از این جا به بعد برای هر کمپلکس بدست آمده محاسبه می شوند
    if len(clusterG1)>2:
        baseClusterCoefficient=ClusterCoefficient.clusterCoefficient(G1)
        if(baseClusterCoefficient==0):
            print(bonacichNode)
            notCCmorethanZeroList.append(bonacichNode)
        # if(baseClusterCoefficient>0):
        for i in clusterG1:
            clusterNodesSet.add(i)
        # print("b=%f"%baseClusterCoefficient)
        evaluateNodesSet.add(bonacichNode)
        num=num+1
        # print("num=%d" % num)
        snap.SaveEdgeList(G1, Adress.adress+"DetectClusters\\%d.txt" % bonacichNode)
    # notCCmorethanZero=set()
    # else:
    #     notCCmorethanZero.add(bonacichNode)

    # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodes,notCCmorethanZero)
    # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodesSet, None)
    # if(bonacichNode==-1):
    #     break
for i in evaluateNodesSet:
    name=Adress.adress+"DetectClusters\\" +str(i)+".txt"
    Merge.deleteThreeLine(name)
nonZero= Merge.Merge(notCCmorethanZeroList)
# nonZero=example.Merge(list(evaluateNodesSet))
for i in nonZero:
    print("i=%d"%i)
    evaluateNodesSet.remove(i)

convertToName.ConvertToName(evaluateNodesSet)
# print(len(clusterNodes))
print(num-1)
# print(numLessThanTwo)
