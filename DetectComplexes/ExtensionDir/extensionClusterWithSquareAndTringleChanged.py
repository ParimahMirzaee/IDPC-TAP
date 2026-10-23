import snap


from SelectSeed import SeedCoefficient
from ExtensionDir import  Functions

from Criterion import ClusterCoefficient , Density
from SelectNextNode import Function
from Other import OtherFunctions
import Adress


def clusterExtention(thereshold,enableThreeNeighbor):
    num=0
    clusterNodesSet=set()
    evaluateNodesSet=set()

    # delete forlder of detectClusters
    folder = Adress.adress + "DetectClusters"
    OtherFunctions.DeleteDirectory(folder)


    # ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, "dip_output_protein_name.txt", 0, 1)
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    # snap.DelDegKNodes(Graph, 1, 1)


    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\krogan2006_core.txt", 0, 1)
    #بدست آوردن دانه ها
    # bonacichNodes=[51]
    # bonacichNodes= functionFirstSeed.selectSeedByBonacichInFirst(Graph, clusterNodesSet)
    # bonacichNodes=example2.selectSeed(Graph)
    # bonacichNode=function2.selectSeedByBonacich(Graph, clusterNodesSet, None)



    bonacichNodes=SeedCoefficient.seedCoefficient(Graph,thereshold)
    # bonacichNodes=SeedCoefficient.largestDegrees(Graph,0)
    # bonacichNodes=SeedCoefficient.largestDegrees()





    noClusteredSeed=set()
    #تا زمانی که پروتئین باقی مانده باشد ادامه دارد.
    # while(len(clusterNodesSet) != snap.CntNonZNodes(Graph)):
    for bonacichNode in bonacichNodes:
        # if len(clusterNodesSet) >= snap.CntNonZNodes(Graph):
        #     break
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
                    # print("true")
                    # baseClusterCoefficient=function.clusterCoefficient(G1)
                    # clusterNodes.add(firstNeighbor)
                    # print("yes")
                else:
                    # print("no")
                    if not exist:
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
                    # result=Function.selectSecondNeighborForExtenionWithBonacich(bonacichNode,secondNeighborVec,Graph)

                    result = Functions.ClusterCoefficientsList(Graph,firstNeighbor, secondNeighborVec)


                    # bonacichNodeFromSecondNeighbor=result[0]
                    # if bonacichNodeFromSecondNeighbor==-1:
                    #     continue
                    # for secondNeighbor in bonacichNodeFromSecondNeighbor:
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

                                    # thirdNeighborSelected=result[1][secondNeighbor]
                                    # thirdNeighbors=Function.selectThirdNeighborWithHighDegree(firstNeighbor,thirdNeighborSelected,Graph)
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

                            #         fourthNeighborVec = Functions.xThNeighbor(Graph, thirdNeighbor, 1)
                                    # for fourthNeighbor in fourthNeighborVec:
                                    #     FirstDensity=Density.Density(G1)
                                    #     if(fourthNeighbor not in clusterG1):
                                    #         G1.AddNode(fourthNeighbor)
                                    #         SecondDensity = Density.Density(G1)
                                    #         if (SecondDensity >= FirstDensity):
                                    #             clusterG1.add(fourthNeighbor)
                                    #         else:
                                    #             G1.DelNode(fourthNeighbor)


                                    # for fourthNeighbor in fourthNeighborVec:
                                    #     baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
                                    #     if(fourthNeighbor not in clusterG1):
                                    #         G1.AddNode(fourthNeighbor)
                                    #         if (ClusterCoefficient.clusterCoefficient(G1) >= baseClusterCoefficient):
                                    #             clusterG1.add(fourthNeighbor)
                                    #         else:
                                    #             G1.DelNode(fourthNeighbor)


                FirstDensity = Density.Density(G1)


        baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)

       #پایان for برای همسایه های اول هر seed



        # print("hhhhh")
        # print(len(clusterG1))
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
        #از این جا به بعد برای هر کمپلکس بدست آمده محاسبه می شوند
        # if len(clusterG1)>2 and baseClusterCoefficient>0:
        # if len(clusterG1)>2 and len(clusterG1)<25:
        if len(clusterG1)>2:
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

            #save edges of clusters *************************
            # snap.SaveEdgeList(G1,name )

        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

        # notCCmorethanZero=set()
        # else:
        #     notCCmorethanZero.add(bonacichNode)

        # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodes,notCCmorethanZero)
        # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodesSet, None)
        # if(bonacichNode==-1):
        #     break


    #     else:
    #         noClusteredSeed.add(bonacichNode)
    #
    # return noClusteredSeed


    # ****************************if just save edges  for clusters not nodes **********************
    # for i in evaluateNodesSet:
    #     name=Adress.adress+"DetectClusters\\" +str(i)+".txt"
    #     Functions.deleteThreeLine(name)
    #




    #******************with merge***************************************
    # from Merge import Merge
    # nonZero=Merge.Merge(list(evaluateNodesSet))
    # for i in nonZero:
    #     print("i=%d"%i)
    #     evaluateNodesSet.remove(i)
    # print("num Clusters : "+str(len(evaluateNodesSet)))
    # convertToName.ConvertToName(evaluateNodesSet)

    #*******************************************************************

    #************************with MergeUseFiles******************************
    # from Merge import MergeUseFiles
    # MergeUseFiles.Merge(1,True)
    # clusters = os.listdir(Adress.adress + "DetectClusters")
    #
    # clusterWithLessThreeNodes=set()
    # for id in clusters:
    #     listNodesName = set()
    #     name = Adress.adress + "DetectClusters\\" + id
    #     with open(name, "r")as f:
    #         for line in enumerate(f):
    #             for i in line[1].split():
    #                 listNodesName.add(i)
    #     #حذف کلاسترهایی با کمتر از ۳ نود
    #     if len(listNodesName)<3 :
    #        clusterWithLessThreeNodes.add(id)
    #        os.remove(Adress.adress + "DetectClusters\\" + id)
    # evaluateClusters = [x for x in clusters if x not in clusterWithLessThreeNodes]
    #
    # print("num Clusters after merge: "+str(len(evaluateClusters)))
    #
    # evaluateClusters=[s[0:-4] for s in evaluateClusters]
    # convertToName.ConvertToName(evaluateClusters)

    #************************************************************************


def clusterExtention2(bonacichNodes, enableThreeNeighbor):
    num = 0
    clusterNodesSet = set()
    evaluateNodesSet = set()

    # delete forlder of detectClusters
    # folder = Adress.adress + "DetectClusters"
    # OtherFunctions.DeleteDirectory(folder)

    # ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, "dip_output_protein_name.txt", 0, 1)
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
    # snap.DelDegKNodes(Graph, 1, 1)

    # Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\krogan2006_core.txt", 0, 1)
    # بدست آوردن دانه ها
    # bonacichNodes=[51]
    # bonacichNodes= functionFirstSeed.selectSeedByBonacichInFirst(Graph, clusterNodesSet)
    # bonacichNodes=example2.selectSeed(Graph)
    # bonacichNode=function2.selectSeedByBonacich(Graph, clusterNodesSet, None)
    # bonacichNodes = SeedCoefficient.seedCoefficient(Graph, thereshold)

    # تا زمانی که پروتئین باقی مانده باشد ادامه دارد.
    # while(len(clusterNodesSet) != snap.CntNonZNodes(Graph)):
    for bonacichNode in bonacichNodes:
        bonacichNode = int(bonacichNode)
        if (bonacichNode not in clusterNodesSet):
            G1 = snap.TUNGraph.New()
            clusterG1 = set()
            G1.AddNode(bonacichNode)
            FirstDensity = 0
            baseClusterCoefficient = 0
            lastBaseClusterCoefficient = 0
            clusterG1.add(bonacichNode)
            firstNeighborVec = Functions.xThNeighbor(Graph, bonacichNode, 1)
            firstNeighborVec = Functions.ClusterCoefficientsList(Graph, bonacichNode, firstNeighborVec)
            # firstNeighborVec=Functions.degreeNodesList(Graph,firstNeighborVec)
            if len(firstNeighborVec) == 0:
                continue
            # یک for برای همسایه‌های اول
            for firstNeighbor in firstNeighborVec:
                if (firstNeighbor != bonacichNode):
                    addedSecondNeighbor = False
                    baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
                    FirstDensity = Density.Density(G1)
                    exist = False
                    if firstNeighbor not in clusterG1:
                        G1.AddNode(firstNeighbor)
                        # clusterG1.add(firstNeighbor)
                        # clusterNodes.add(firstNeighbor)
                    else:
                        exist = True

                    sub = 0  # اشتراک
                    # تمام همسایه های اول اضافه می‌شوند و چک می شود ک آیا با نودهای دیگر که درون گراف هستند یا درواقع با نودهای همسایه اول دیگر رابطه دارند یا خیر؟
                    for eachNode in G1.Nodes():
                        if (Functions.isEdgeInGraph(eachNode.GetId(), firstNeighbor, Graph)):
                            G1.AddEdge(eachNode.GetId(), firstNeighbor)
                            sub += 1

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

                    SecondDensity = Density.Density(G1)
                    if (SecondDensity >= FirstDensity):
                        clusterG1.add(firstNeighbor)
                        # print("true")
                        # baseClusterCoefficient=function.clusterCoefficient(G1)
                        # clusterNodes.add(firstNeighbor)
                        # print("yes")
                    else:
                        # print("no")
                        if not exist:
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

                    # بدست آوردن همسایه های دوم با عبور از این همسایه اول
                    # یا در واقع همسایه های اول همسایه اول مشخص شده
                    secondNeighborVec = Functions.xThNeighbor(Graph, firstNeighbor, 1)

                    # چک شود ک به جز firstneighbor همسایه دیگری داشته باشد
                    if len(secondNeighborVec) != 1:
                        # حالا باید طبق bonacich چندتا از نودهارو انتخا کنم
                        # result=Function.selectSecondNeighborForExtenionWithBonacich(bonacichNode,secondNeighborVec,Graph)

                        result = Functions.ClusterCoefficientsList(Graph, firstNeighbor, secondNeighborVec)

                        # bonacichNodeFromSecondNeighbor=result[0]
                        # if bonacichNodeFromSecondNeighbor==-1:
                        #     continue
                        # for secondNeighbor in bonacichNodeFromSecondNeighbor:
                        for secondNeighbor in result:
                            if (secondNeighbor != bonacichNode):
                                if (Functions.isEdgeInGraph(bonacichNode, secondNeighbor, Graph)):
                                    # مثلث ببین نود اصلی و همسایه دوم ایجاد شده است
                                    addedSecondNeighbor = True
                                    if secondNeighbor not in clusterG1:
                                        G1.AddNode(secondNeighbor)
                                        clusterG1.add(secondNeighbor)
                                        # clusterNodes.add(secondNeighbor)
                                    for eachNode in G1.Nodes():
                                        if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                            G1.AddEdge(eachNode.GetId(), secondNeighbor)

                                    # #چه مثلث قبلی ایجاد شده بود چ نشده بود باید همسایه سوم را نیز بررسی کنیم.
                                    if enableThreeNeighbor:
                                        #     if enableThreeNeighbor and len(clusterG1)<10:
                                        thirdNeighborVec = Functions.xThNeighbor(Graph, secondNeighbor, 1)
                                        # thirdNeighbors = Function.selectSecondNeighborForExtenionWithBonacich(secondNeighbor, thirdNeighborVec, Graph)
                                        thirdNeighbors = Functions.ClusterCoefficientsList(Graph, secondNeighbor,
                                                                                           thirdNeighborVec)

                                        # thirdNeighborSelected=result[1][secondNeighbor]
                                        # thirdNeighbors=Function.selectThirdNeighborWithHighDegree(firstNeighbor,thirdNeighborSelected,Graph)
                                        if (thirdNeighbors == -1):
                                            continue

                                        if len(thirdNeighbors) != 1:
                                            for thirdNeighbor in thirdNeighbors:
                                                triangle = square = False
                                                # if (thirdNeighbor != bonacichNode):
                                                if (Functions.isEdgeInGraph(bonacichNode, thirdNeighbor, Graph)):
                                                    # مربع ببین نود اصلی و همسایه سوم ایجاد شده است
                                                    if thirdNeighbor not in clusterG1:
                                                        G1.AddNode(thirdNeighbor)
                                                        clusterG1.add(thirdNeighbor)
                                                        # clusterNodes.add(thirdNeighbor)
                                                    square = True
                                                    for eachNode in G1.Nodes():
                                                        if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor,
                                                                                    Graph)):
                                                            G1.AddEdge(eachNode.GetId(), thirdNeighbor)

                                                elif (Functions.isEdgeInGraph(firstNeighbor, thirdNeighbor, Graph)):
                                                    # مثلث ببین همسایه اول و همسایه سوم ایجاد شده است
                                                    if thirdNeighbor not in clusterG1:
                                                        G1.AddNode(thirdNeighbor)
                                                        clusterG1.add(thirdNeighbor)
                                                        # clusterNodes.add(thirdNeighbor)
                                                    triangle = True
                                                    for eachNode in G1.Nodes():
                                                        if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor,
                                                                                    Graph)):
                                                            G1.AddEdge(eachNode.GetId(), thirdNeighbor)

                                                if ((triangle or square) and not addedSecondNeighbor):
                                                    if secondNeighbor not in clusterG1:
                                                        G1.AddNode(secondNeighbor)
                                                        clusterG1.add(secondNeighbor)
                                                        # clusterNodes.add(secondNeighbor)
                                                    addedSecondNeighbor = True
                                                    for eachNode in G1.Nodes():
                                                        if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor,
                                                                                    Graph)):
                                                            G1.AddEdge(eachNode.GetId(), secondNeighbor)

                                #         fourthNeighborVec = Functions.xThNeighbor(Graph, thirdNeighbor, 1)
                                # for fourthNeighbor in fourthNeighborVec:
                                #     FirstDensity=Density.Density(G1)
                                #     if(fourthNeighbor not in clusterG1):
                                #         G1.AddNode(fourthNeighbor)
                                #         SecondDensity = Density.Density(G1)
                                #         if (SecondDensity >= FirstDensity):
                                #             clusterG1.add(fourthNeighbor)
                                #         else:
                                #             G1.DelNode(fourthNeighbor)

                                # for fourthNeighbor in fourthNeighborVec:
                                #     baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
                                #     if(fourthNeighbor not in clusterG1):
                                #         G1.AddNode(fourthNeighbor)
                                #         if (ClusterCoefficient.clusterCoefficient(G1) >= baseClusterCoefficient):
                                #             clusterG1.add(fourthNeighbor)
                                #         else:
                                #             G1.DelNode(fourthNeighbor)

                    FirstDensity = Density.Density(G1)

            baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)

            # پایان for برای همسایه های اول هر seed

            # print("hhhhh")
            # print(len(clusterG1))
            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
            # از این جا به بعد برای هر کمپلکس بدست آمده محاسبه می شوند
            # if len(clusterG1)>2 and baseClusterCoefficient>0:
            # if len(clusterG1)>2 and len(clusterG1)<25:
            if len(clusterG1) > 2:
                baseClusterCoefficient = ClusterCoefficient.clusterCoefficient(G1)
                # if(baseClusterCoefficient==0):
                #     print(bonacichNode)
                #     notCCmorethanZeroList.append(bonacichNode)
                # if(baseClusterCoefficient>0):
                for i in clusterG1:
                    clusterNodesSet.add(i)
                # print("b=%f"%baseClusterCoefficient)
                evaluateNodesSet.add(bonacichNode)
                num = num + 1
                # print("num=%d" % num)
                name = Adress.adress + "DetectClusters2\\" + str(bonacichNode) + ".txt"

                # save nodes of clusters ************************
                file = open(name, "w")
                for node in clusterG1:
                    file.write(str(node) + "\n")
                file.close()

                # save edges of clusters *************************
                # snap.SaveEdgeList(G1,name )

            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

            # notCCmorethanZero=set()
            # else:
            #     notCCmorethanZero.add(bonacichNode)

            # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodes,notCCmorethanZero)
            # bonacichNode = function2.selectSeedByBonacich(Graph, clusterNodesSet, None)
            # if(bonacichNode==-1):
            #     break




    # ****************************if just save edges  for clusters not nodes **********************
    # for i in evaluateNodesSet:
    #     name=Adress.adress+"DetectClusters\\" +str(i)+".txt"
    #     Functions.deleteThreeLine(name)
    #

    # ******************with merge***************************************
    # from Merge import Merge
    # nonZero=Merge.Merge(list(evaluateNodesSet))
    # for i in nonZero:
    #     print("i=%d"%i)
    #     evaluateNodesSet.remove(i)
    # print("num Clusters : "+str(len(evaluateNodesSet)))
    # convertToName.ConvertToName(evaluateNodesSet)

    # *******************************************************************

    # ************************with MergeUseFiles******************************
    # from Merge import MergeUseFiles
    # MergeUseFiles.Merge(1,True)
    # clusters = os.listdir(Adress.adress + "DetectClusters")
    #
    # clusterWithLessThreeNodes=set()
    # for id in clusters:
    #     listNodesName = set()
    #     name = Adress.adress + "DetectClusters\\" + id
    #     with open(name, "r")as f:
    #         for line in enumerate(f):
    #             for i in line[1].split():
    #                 listNodesName.add(i)
    #     #حذف کلاسترهایی با کمتر از ۳ نود
    #     if len(listNodesName)<3 :
    #        clusterWithLessThreeNodes.add(id)
    #        os.remove(Adress.adress + "DetectClusters\\" + id)
    # evaluateClusters = [x for x in clusters if x not in clusterWithLessThreeNodes]
    #
    # print("num Clusters after merge: "+str(len(evaluateClusters)))
    #
    # evaluateClusters=[s[0:-4] for s in evaluateClusters]
    # convertToName.ConvertToName(evaluateClusters)

    # ************************************************************************