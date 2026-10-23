import Weighing
import snap
import Adress
import priority
from PickleData import convertToName
from Evaluate import Evaluate
from Other import OtherFunctions

T=0.2
d=2
Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\dip_output_protein_name.txt", 0, 1)

#وزن دهی تمام نودها
listNodes=Weighing.weightingNodes(Graph)
cluster=set()
folder = Adress.adress + "IpcaClusters"
OtherFunctions.DeleteDirectory(folder)


while len(listNodes)!=0:
    seed=listNodes[0]
    cluster.add(seed)  #seed
    while True:
        neighbors=set()
        #بدست آوردن همسایه های کلاستر جدید
        for node in cluster:
            NodeVec = snap.TIntV()
            snap.GetNodesAtHop(Graph, node, 1, NodeVec, False)
            for item in NodeVec:
                if item not in cluster:
                    neighbors.add(item)

        test=priority.testNodes(Graph,cluster,neighbors,T,d)
        if test==False:
            if len(cluster)>2:
                name = Adress.adress + "IpcaClusters\\" + str(seed) + ".txt"
                # save nodes of clusters ************************
                file = open(name, "w")
                for node in cluster:
                    file.write(str(node) + "\n")
                    if node in listNodes:
                        listNodes.remove(node)
                file.close()
                cluster=set()

            else:
                if seed in listNodes:
                    listNodes.remove(seed)

            print(len(listNodes))
            break
        else:
            cluster=test

convertToName.ConvertToName("IpcaClusters")
Evaluate.Evaluate()