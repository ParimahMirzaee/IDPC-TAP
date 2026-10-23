import snap
from SelectSeed import SeedCoefficient
from Extension import  Functions
from Criterion import ClusterCoefficient , Density
from SelectNextNode import Function
from Other import OtherFunctions
import Adress



#with all nodes and with condition for first nodes
def clusterExtention(thereshold,enableThreeNeighbor):
    num=0
    clusterNodesSet=set()
    evaluateNodesSet=set()


    #delete forlder of detectClusters
    folder = Adress.adress+"DetectClusters"
    OtherFunctions.DeleteDirectory(folder)



    setUGraphNodes=set()
    # ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    UGraph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)


    #تا زمانی که پروتئین باقی مانده باشد ادامه دارد.
    while(len(clusterNodesSet) != snap.CntNonZNodes(Graph)):
    # for bonacichNode in bonacichNodes:

        bonacichNodes = SeedCoefficient.seedCoefficient(UGraph, thereshold)
        bonacichNode=int(bonacichNodes.pop())

        if(bonacichNode not in clusterNodesSet):
            G1 = snap.TUNGraph.New()
            clusterG1=set()
            G1.AddNode(bonacichNode)
            clusterG1.add(bonacichNode)
            firstNeighborVec=Functions.xThNeighbor(Graph, bonacichNode, 1)
            firstNeighborVec=Functions.ClusterCoefficientsList(Graph,bonacichNode,firstNeighborVec)
            # firstNeighborVec=Functions.degreeNodesList(Graph,firstNeighborVec)
            if len(firstNeighborVec)==0:
                continue
            # یک for برای همسایه‌های اول
            for firstNeighbor in firstNeighborVec:
                if(firstNeighbor!= bonacichNode):
                    addedSecondNeighbor=False
                    baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
                    FirstDensity = Density.Density(G1)
                    exist = False



                    if firstNeighbor not in clusterG1:
                        G1.AddNode(firstNeighbor)
                        # clusterG1.add(firstNeighbor)
                        # clusterNodes.add(firstNeighbor)
                    else:
                        exist=True


                    sub=0 # اشتراک
                    #تمام همسایه های اول اضافه می‌شوند و چک می شود ک آیا با نودهای دیگر که درون گراف هستند یا درواقع با نودهای همسایه اول دیگر رابطه دارند یا خیر؟
                    for eachNode in G1.Nodes():
                        if (Functions.isEdgeInGraph(eachNode.GetId(), firstNeighbor, Graph)):
                            G1.AddEdge(eachNode.GetId(), firstNeighbor)
                            sub+=1


                    # add first neighbor due to density
                    # SecondDensity=Density.Density(G1)
                    # if(SecondDensity>=FirstDensity):
                        clusterG1.add(firstNeighbor)
                    # else:
                    #     if not exist:
                    #         G1.DelNode(firstNeighbor)
                    #     continue

                    #بدست آوردن همسایه های دوم با عبور از این همسایه اول
                    #یا در واقع همسایه های اول همسایه اول مشخص شده
                    secondNeighborVec = Functions.xThNeighbor(Graph, firstNeighbor, 1)

                    # چک شود ک به جز firstneighbor همسایه دیگری داشته باشد
                    if len(secondNeighborVec)!=1:
                        #حالا باید طبق bonacich چندتا از نودهارو انتخا کنم
                        result = Functions.ClusterCoefficientsList(Graph,firstNeighbor, secondNeighborVec)
                        for secondNeighbor in result:
                            if (secondNeighbor != bonacichNode):
                                if(Functions.isEdgeInGraph(bonacichNode, secondNeighbor, Graph)):
                                    #مثلث ببین نود اصلی و همسایه دوم ایجاد شده است
                                    addedSecondNeighbor=True
                                    if secondNeighbor not in clusterG1:
                                        G1.AddNode(secondNeighbor)
                                        clusterG1.add(secondNeighbor)
                                        # clusterNodes.add(secondNeighbor)
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), secondNeighbor)


                                # #چه مثلث قبلی ایجاد شده بود چ نشده بود باید همسایه سوم را نیز بررسی کنیم.
                                    if enableThreeNeighbor :
                                #     if enableThreeNeighbor and len(clusterG1)<10:
                                        thirdNeighborVec = Functions.xThNeighbor(Graph, secondNeighbor, 1)
                                        # thirdNeighbors = Function.selectSecondNeighborForExtenionWithBonacich(secondNeighbor, thirdNeighborVec, Graph)
                                        thirdNeighbors=Functions.ClusterCoefficientsList(Graph,secondNeighbor,thirdNeighborVec)
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

           #پایان for برای همسایه های اول هر seed



            # print("hhhhh")
            # print(len(clusterG1))
            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
            #از این جا به بعد برای هر کمپلکس بدست آمده محاسبه می شوند
            # if len(clusterG1)>2 and baseClusterCoefficient>0:
            # if len(clusterG1)>2 and len(clusterG1)<25:
            # if len(clusterG1)>2:
            baseClusterCoefficient=ClusterCoefficient.clusterCoefficient(G1)
            # if(baseClusterCoefficient==0):
            #     print(bonacichNode)
            #     notCCmorethanZeroList.append(bonacichNode)
            # if(baseClusterCoefficient>0):
            for i in clusterG1:
                clusterNodesSet.add(i)
            # print("b=%f"%baseClusterCoefficient)
            evaluateNodesSet.add(bonacichNode)
            num=num+1
            # print("num=%d" % num)
            name=Adress.adress+"DetectClusters\\"+str(bonacichNode)+".txt"

            # save nodes of clusters ************************
            file=open(name,"w")
            for node in clusterG1:
                file.write(str(node) + "\n")
            file.close()


            for node in clusterNodesSet:
                if node not in setUGraphNodes:
                    UGraph.DelNode(node)
                    setUGraphNodes.add(node)
            # print(str(snap.CntNonZNodes(UGraph)))



#with all nodes and add first nodes if second nodes added
def clusterExtentionWithConditionFirstNeighbors(thereshold,enableThreeNeighbor):
    num=0
    clusterNodesSet=set()
    evaluateNodesSet=set()


    #delete forlder of detectClusters
    folder = Adress.adress+"DetectClusters"
    OtherFunctions.DeleteDirectory(folder)



    setUGraphNodes=set()
    # ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    UGraph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)


    #تا زمانی که پروتئین باقی مانده باشد ادامه دارد.
    while(len(clusterNodesSet) != snap.CntNonZNodes(Graph)):
    # for bonacichNode in bonacichNodes:

        bonacichNodes = SeedCoefficient.seedCoefficient(UGraph, thereshold)
        bonacichNode=int(bonacichNodes.pop())

        if(bonacichNode not in clusterNodesSet):
            G1 = snap.TUNGraph.New()
            clusterG1=set()
            G1.AddNode(bonacichNode)
            clusterG1.add(bonacichNode)
            firstNeighborVec=Functions.xThNeighbor(Graph, bonacichNode, 1)
            firstNeighborVec=Functions.ClusterCoefficientsList(Graph,bonacichNode,firstNeighborVec)
            # firstNeighborVec=Functions.degreeNodesList(Graph,firstNeighborVec)
            if len(firstNeighborVec)==0:
                continue
            # یک for برای همسایه‌های اول
            for firstNeighbor in firstNeighborVec:
                if(firstNeighbor!= bonacichNode):
                    addedSecondNeighbor=False

                    if firstNeighbor not in clusterG1:
                        G1.AddNode(firstNeighbor)
                        exist=False
                        # clusterG1.add(firstNeighbor)
                        # clusterNodes.add(firstNeighbor)
                    else:
                        exist=True


                    sub=0 # اشتراک
                    #تمام همسایه های اول اضافه می‌شوند و چک می شود ک آیا با نودهای دیگر که درون گراف هستند یا درواقع با نودهای همسایه اول دیگر رابطه دارند یا خیر؟
                    for eachNode in G1.Nodes():
                        if (Functions.isEdgeInGraph(eachNode.GetId(), firstNeighbor, Graph)):
                            G1.AddEdge(eachNode.GetId(), firstNeighbor)
                            sub+=1


                    # add first neighbor due to density
                    # SecondDensity=Density.Density(G1)
                    # if(SecondDensity>=FirstDensity):
                        clusterG1.add(firstNeighbor)
                    # else:
                    #     if not exist:
                    #         G1.DelNode(firstNeighbor)
                    #     continue

                    #بدست آوردن همسایه های دوم با عبور از این همسایه اول
                    #یا در واقع همسایه های اول همسایه اول مشخص شده
                    secondNeighborVec = Functions.xThNeighbor(Graph, firstNeighbor, 1)

                    # چک شود ک به جز firstneighbor همسایه دیگری داشته باشد
                    if len(secondNeighborVec)!=1:
                        #حالا باید طبق bonacich چندتا از نودهارو انتخا کنم
                        result = Functions.ClusterCoefficientsList(Graph,firstNeighbor, secondNeighborVec)
                        for secondNeighbor in result:
                            if (secondNeighbor != bonacichNode):
                                if(Functions.isEdgeInGraph(bonacichNode, secondNeighbor, Graph)):
                                    #مثلث ببین نود اصلی و همسایه دوم ایجاد شده است
                                    addedSecondNeighbor=True
                                    if secondNeighbor not in clusterG1:
                                        G1.AddNode(secondNeighbor)
                                        clusterG1.add(secondNeighbor)
                                        # clusterNodes.add(secondNeighbor)
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), secondNeighbor)


                                # #چه مثلث قبلی ایجاد شده بود چ نشده بود باید همسایه سوم را نیز بررسی کنیم.
                                    if enableThreeNeighbor :
                                #     if enableThreeNeighbor and len(clusterG1)<10:
                                        thirdNeighborVec = Functions.xThNeighbor(Graph, secondNeighbor, 1)
                                        # thirdNeighbors = Function.selectSecondNeighborForExtenionWithBonacich(secondNeighbor, thirdNeighborVec, Graph)
                                        thirdNeighbors=Functions.ClusterCoefficientsList(Graph,secondNeighbor,thirdNeighborVec)
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


                        if not addedSecondNeighbor:
                            if not exist:
                                G1.DelNode(firstNeighbor)
                                clusterG1.remove(firstNeighbor)
                            else:
                                G1.DelNode(firstNeighbor)
           #پایان for برای همسایه های اول هر seed



            # print("hhhhh")
            # print(len(clusterG1))
            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
            #از این جا به بعد برای هر کمپلکس بدست آمده محاسبه می شوند
            # if len(clusterG1)>2 and baseClusterCoefficient>0:
            # if len(clusterG1)>2 and len(clusterG1)<25:
            # if len(clusterG1)>2:
            baseClusterCoefficient=ClusterCoefficient.clusterCoefficient(G1)
            # if(baseClusterCoefficient==0):
            #     print(bonacichNode)
            #     notCCmorethanZeroList.append(bonacichNode)
            # if(baseClusterCoefficient>0):
            for i in clusterG1:
                clusterNodesSet.add(i)
            # print("b=%f"%baseClusterCoefficient)
            evaluateNodesSet.add(bonacichNode)
            num=num+1
            # print("num=%d" % num)
            name=Adress.adress+"DetectClusters\\"+str(bonacichNode)+".txt"

            # save nodes of clusters ************************
            file=open(name,"w")
            for node in clusterG1:
                file.write(str(node) + "\n")
            file.close()


            for node in clusterNodesSet:
                if node not in setUGraphNodes:
                    UGraph.DelNode(node)
                    setUGraphNodes.add(node)
            # print(str(snap.CntNonZNodes(UGraph)))