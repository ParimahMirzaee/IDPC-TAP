import snap
from SelectSeed import SeedCoefficient
from ExtensionDir import  Functions
from Criterion import ClusterCoefficient , Density
from Other import OtherFunctions
import Adress


def clusterExtention(thereshold,enableThreeNeighbor):
    num=0
    clusterNodesSet=set()
    evaluateNodesSet=set()


    #delete forlder of detectClusters
    folder = Adress.adress+"NewDetectClusters"
    OtherFunctions.DeleteDirectory(folder)



    # ارزیابی با اضافه کردن نودها به مجموعه نودهای ارزیابی نشده و حذف نکردن آنها و روش extension معمولی
    Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)


    # bonacichNodes=SeedCoefficient.seedCoefficient(Graph,thereshold)
    # bonacichNodes=SeedCoefficient.degreeCloseness(Graph)
    # bonacichNodes=SeedCoefficient.closeBetweenNess(Graph)


    for bonacichNode in range(0,4928):
    # for bonacichNode in bonacichNodes:
    #     bonacichNode=4927
        bonacichNode=int(bonacichNode)
        G1 = snap.TUNGraph.New()
        clusterG1=set()
        G1.AddNode(bonacichNode)
        clusterG1.add(bonacichNode)
        firstNeighborVec=Functions.xThNeighbor(Graph, bonacichNode, 1)
        # firstNeighborVec=Functions.ClusterCoefficientsList(Graph,bonacichNode,firstNeighborVec)
        firstNeighborVec=SeedCoefficient.largestDegreesWithBonacich(Graph,0,firstNeighborVec)


        if len(firstNeighborVec)==0:
            continue


        # یک for برای همسایه‌های اول
        for firstNeighbor in firstNeighborVec:
            if(firstNeighbor!= bonacichNode):
                FirstDensity = Density.Density(G1)
                exist = False
                if firstNeighbor not in clusterG1:
                    G1.AddNode(firstNeighbor)
                else:
                    exist=True

                sub=0 # اشتراک
                #تمام همسایه های اول اضافه می‌شوند و چک می شود ک آیا با نودهای دیگر که درون گراف هستند یا درواقع با نودهای همسایه اول دیگر رابطه دارند یا خیر؟
                for eachNode in G1.Nodes():
                    if (Functions.isEdgeInGraph(eachNode.GetId(), firstNeighbor, Graph)):
                        G1.AddEdge(eachNode.GetId(), firstNeighbor)
                        sub+=1
                # add first neighbor due to density
                SecondDensity=Density.Density(G1)
                if(SecondDensity>=FirstDensity):
                    clusterG1.add(firstNeighbor)
                else:
                    if not exist:
                        G1.DelNode(firstNeighbor)
                    continue

                #بدست آوردن همسایه های دوم با عبور از این همسایه اول
                #یا در واقع همسایه های اول همسایه اول مشخص شده
                secondNeighborVec = Functions.xThNeighbor(Graph, firstNeighbor, 1)

                # چک شود ک به جز firstneighbor همسایه دیگری داشته باشد
                if len(secondNeighborVec)!=1:
                    #حالا باید طبق Coefficient چندتا از نودهارو انتخا کنم
                    result = Functions.ClusterCoefficientsList(Graph,firstNeighbor, secondNeighborVec)

                    for secondNeighbor in result:
                        if (secondNeighbor != bonacichNode):
                            if(Functions.isEdgeInGraph(bonacichNode, secondNeighbor, Graph)):
                                #مثلث ببین نود اصلی و همسایه دوم ایجاد شده است
                                if secondNeighbor not in clusterG1:
                                    G1.AddNode(secondNeighbor)
                                    clusterG1.add(secondNeighbor)
                                for eachNode in G1.Nodes():
                                    if (Functions.isEdgeInGraph(eachNode.GetId(), secondNeighbor, Graph)):
                                        G1.AddEdge(eachNode.GetId(), secondNeighbor)


                            # #اگر مثلث قبلی ایجاد شده بود باید همسایه سوم را نیز بررسی کنیم.
                                if enableThreeNeighbor :
                                    thirdNeighborVec = Functions.xThNeighbor(Graph, secondNeighbor, 1)
                                    thirdNeighbors=Functions.ClusterCoefficientsList(Graph,secondNeighbor,thirdNeighborVec)

                                    if(thirdNeighbors==-1):
                                        continue

                                    if len(thirdNeighbors)!=1:
                                        for thirdNeighbor in thirdNeighbors:
                                            if (Functions.isEdgeInGraph(bonacichNode, thirdNeighbor, Graph)):
                                                # مربع بین نود اصلی و همسایه سوم ایجاد شده است
                                                if thirdNeighbor not in clusterG1:
                                                    G1.AddNode(thirdNeighbor)
                                                    clusterG1.add(thirdNeighbor)
                                                for eachNode in G1.Nodes():
                                                    if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor, Graph)):
                                                        G1.AddEdge(eachNode.GetId(), thirdNeighbor)
                                            elif (Functions.isEdgeInGraph(firstNeighbor, thirdNeighbor, Graph)):
                                                # مثلث ببین همسایه اول و همسایه سوم ایجاد شده است
                                                if thirdNeighbor not in clusterG1:
                                                    G1.AddNode(thirdNeighbor)
                                                    clusterG1.add(thirdNeighbor)
                                                for eachNode in G1.Nodes():
                                                    if (Functions.isEdgeInGraph(eachNode.GetId(), thirdNeighbor, Graph)):
                                                        G1.AddEdge(eachNode.GetId(), thirdNeighbor)


       #پایان for برای همسایه های اول هر seed




        for i in clusterG1:
            clusterNodesSet.add(i)
        evaluateNodesSet.add(bonacichNode)
        num=num+1
        name=Adress.adress+"NewDetectClusters\\"+str(bonacichNode)+".txt"

        # save nodes of clusters ************************
        file=open(name,"w")
        for node in clusterG1:
            file.write(str(node) + "\n")
        file.close()