from ExtensionDir import extensionClusterWithSquareAndTringleChanged
from PickleData import convertToName
from Evaluate import Evaluate
# from Merge import  Merge
import snap
import Adress


# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# Count = snap.CntDegNodes(Graph, 1)
# print("UnDirected Graph: Count of nodes with degree 1 is %d" % Count)
# i=0
# for NI in Graph.Nodes():
#     if NI.GetOutDeg() == 1:
#         i+=1
#     elif NI.GetInDeg() == 1:
#         i+=1
# snap.DelDegKNodes(Graph, 1, 1)


# print(i)
# Count = snap.CntDegNodes(Graph, 1)
# print("UnDirected Graph: Count of nodes with degree 1 is %d" % Count)

# import sys
# sys.stdout = open("test.txt", "w")
#
# ccThereshold=[0.05,0.23,0.3,0.5]
# enableThreeNeighbor=[True,False]
#
# for k in enableThreeNeighbor:
#     for i in ccThereshold:
#         print("********************************************")
#         print("enableThreeNeighbor :"+str(k))
#         print(str(i))
#
#         extensionClusterWithSquareAndTringleChanged.clusterExtention(i,k)
#
#         folder=["DetectClusters","MergeClusters","MergeClusters2","MergeClusters3","MergeClusters4"]
#
#         convertToName.ConvertToName(folder[0])
#         Evaluate.Evaluate()
#
#         for j in range(3):
#             print("merge "+str(j+1))
#             folderRes=folder[j]
#             folderDes=folder[j+1]
#             Merge.Merge(folderRes,folderDes)
#             convertToName.ConvertToName(folderDes)
#             Evaluate.Evaluate()
#
# sys.stdout.close()

# import sys
# sys.stdout = open("resultAllKrogan.txt", "w")
# from ExtensionDir import ExtensionCores
# from Merge import Merge
# thresholds=[0.05,0.1,0.18,0.3,0.5,0.7]
# thirdNeighbor=[False,True]
# extensionCore=[False ,True]
# numMerge=4

# for threshold in thresholds:
#     print("***************************************")
#     for extension in extensionCore:
#         for third in thirdNeighbor:
#             print("threshold: "+str(threshold)+" with third neighbor: "+str(third)+" with extensionCore: "+str(extension))
#             extensionClusterWithSquareAndTringleChanged.clusterExtention(threshold,third)
#             if extension:
#                 ExtensionCores.ExtensionCore("DetectClusters")
#                 mergeFile=["ExtensionCores","MergeClusters","MergeClusters2","MergeClusters3","MergeClusters4"]
#                 for i in range(numMerge):
#                     if i==0:
#                         print("without merge ")
#                         convertToName.ConvertToName("ExtensionCores")
#                         Evaluate.Evaluate()
#                     else:
#                         print(" merge: " + str(i))
#                         Merge.Merge(mergeFile[i],mergeFile[i+1])
#                         convertToName.ConvertToName(mergeFile[i+1])
#                         Evaluate.Evaluate()
#                 print("############################")
#
#             else:
#                 mergeFile = ["DetectClusters", "MergeClusters", "MergeClusters2", "MergeClusters3", "MergeClusters4"]
#                 for i in range(numMerge):
#                     if i == 0:
#                         print("without merge ")
#                         convertToName.ConvertToName("DetectClusters")
#                         Evaluate.Evaluate()
#
#                     else:
#                         print(" merge: " + str(i))
#                         Merge.Merge(mergeFile[i], mergeFile[i + 1])
#                         convertToName.ConvertToName(mergeFile[i + 1])
#                         Evaluate.Evaluate()
#                 print("############################")
# sys.stdout.close()

#***************************************************************************کد اصلیییییییییییییییییییییییی*************************
# from ExtensionDir import extensionClusterWithSquareAndTringleChanged2
# extensionClusterWithSquareAndTringleChanged2.clusterExtention(0,True)
# convertToName.ConvertToName("DetectClusters2")
# Evaluate.Evaluate()
# *****************************************************************************************************************
# from ExtensionDir import NewExtension2
# NewExtension2.clusterExtention(0,True)
convertToName.ConvertToName("NewDetectClusters")
Evaluate.Evaluate()


# استفاده از کلاسترهای قبلی تولید شده
# from SelectSeed import SeedCoefficient
# import os
# from shutil import copyfile
# thereshold=0
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# bonacichNodes = SeedCoefficient.seedCoefficient(Graph, thereshold)
# print(len(bonacichNodes))
# for i in bonacichNodes:
#     name = Adress.adress + "DetectClusters2\\" + str(i) + ".txt"
#     dst=Adress.adress+"DetectClusters3\\"
#     if os.path.isfile(name):
#         copyfile(name, dst+str(i) + ".txt")
#
# convertToName.ConvertToName("DetectClusters3")
# Evaluate.Evaluate()


#حذف کلاستر های با کمتر از ۲ پروتين

# import os
#
# bonacichNodes = os.listdir(Adress.adress + "DetectClusters3")
# for id in bonacichNodes:
#     predictComplex = set()
#     id = int(id[0:-4])
#     name = Adress.adress + "DetectClusters3\\" + str(id) + ".txt"
#     with open(name, "r") as file:
#         for line in file:
#             predictComplex.add(line)
#     if len(predictComplex)<=2:
#         os.remove(name)
#
# convertToName.ConvertToName("DetectClusters3")
# Evaluate.Evaluate()


# نوشتن نودهای کلاستر شده در یک فایل

# import os
# predictComplex = set()
# dst=Adress.adress+"ClusterNodes"
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# bonacichNodes = os.listdir(Adress.adress + "DetectClusters2")
# print(len(bonacichNodes))
# for i in bonacichNodes:
#     a=set()
#     name = Adress.adress + "DetectClusters2\\" + str(i)
#     with open(name, "r") as file:
#         for line in file:
#             a.add(line)
#     if len(a)>2:
#         with open(name, "r") as file:
#             for line in file:
#                 predictComplex.add(line)
# string=""
# fileOut = open(dst, 'w')
# print(len(predictComplex))
# for i in predictComplex:
#     string = string + i
# fileOut.write(string)
# fileOut.close()



# def diameter(Graph,cluster,node,threshold):
#     NIdV = snap.TIntV()
#     cluster.add(node)
#     for node in cluster:
#         NIdV.Add(node)
#     SubGraph = snap.GetSubGraph(Graph, NIdV)
#     if snap.GetBfsFullDiam(SubGraph, len(cluster), False) <=threshold:
#         return True
#     else:
#         return False
#
#
# def extension(Graph):
#     # همسایه های نودهای کلاستر به عنوان کاندید بدست می آیند
#     dest = Adress.adress+"ExtensionClusterFromBaseArticle\\"
#     a = 1
#     candidateNodes=set()
#     for i in CV:
#         NodeVec = snap.TIntV()
#         snap.GetNodesAtHop(Graph, i, 1, NodeVec, False)
#         for i in NodeVec:
#             # if i not in clusterNodes:
#             if i not in CV:
#                 candidateNodes.add(i)
#
#     selectNodes = dict()
#     for u in candidateNodes:
#         uNeighbors=set()
#         NodeVec = snap.TIntV()
#         snap.GetNodesAtHop(Graph, u, 1, NodeVec, False)
#         for i in NodeVec:
#             uNeighbors.add(i)
#
#         up=uNeighbors.intersection(CV)
#         NC=(a*(len(up)/len(CV)))+((1-a)*(len(up)/len(uNeighbors)))
#         if NC>0.2 and diameter(Graph,CV,u,2):
#             selectNodes[u]=NC
#     if len(selectNodes)>0:
#         sort= {k: v for k, v in sorted(selectNodes.items(), key=lambda item: item[1],reverse=True)}
#         addedNode=list(sort.keys())[0]
#         CV.add(addedNode)
#         clusterNodes.add(addedNode)
#         extension(Graph)
#     else:
#         string = ""
#         # if(len(CV)>2):
#         for i in CV:
#             string = string + str(i) + "\n"
#         fileOut = open(dest + str(cluster)+".txt", 'w')
#         fileOut.write(string)
#         fileOut.close()
#         return







# بر اساس مقاله اصلی بیایم و کلاستر های موجود رو گسترش بدیم
import os
import snap
from SelectSeed import SeedCoefficient
# clusterNodes=set()
# name = Adress.adress + "ClusterNodes"
#
# with open(name, "r") as file:
#     for line in file:
#         clusterNodes.add(int(line[0:-1]))
#
# *****************************************************************************************\
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# # bonacichNodes = os.listdir(Adress.adress + "DetectClusters2")
# # BNodes = SeedCoefficient.closeBetweenNess(Graph)
# BNodes = SeedCoefficient.degreeClusterCoefficient(Graph)
# # فقط سیدهایی انتخاب میشن که گسترش پیدا نکردن
# bonacichNodes=[]
# clusterNodes=set()
# for cluster in BNodes:
# # for cluster in range(4928):
#     if cluster not in clusterNodes:
#         bonacichNodes.append(cluster)
#         resource = Adress.adress + "DetectClusters2\\" + str(cluster)+".txt"
#         with open(resource, "r") as file:
#             for line in file:
#                 clusterNodes.add(int(line[0:-1]))
#
# for cluster in bonacichNodes:
#     if len(clusterNodes)==4928:
#         break
#     CV=set()
#     candidateNodes=set()
#     resource = Adress.adress + "DetectClusters2\\" + str(cluster)+".txt"
#     with open(resource, "r") as file:
#         for line in file:
#             CV.add(int(line[0:-1]))
#             # clusterNodes.add(int(line[0:-1]))
#
#     extension(Graph)
#
#
#
# convertToName.ConvertToName("ExtensionClusterFromBaseArticle")
# Evaluate.Evaluate()



# select good clusters and evaluate them
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# DegToCCfV = snap.TFltPrV()
# result = snap.GetClustCfAll(Graph,DegToCCfV)
# print("average clustering coefficient", result[0])
#
#
# BNodes = os.listdir(Adress.adress + "DetectClusters2")
# # فقط سیدهایی انتخاب میشن که گسترش پیدا نکردن
# bonacichNodes=[]
# clusterNodes=set()
# num=0
# for cluster in BNodes:
#     # if len(clusterNodes)!=4928:
#     resource = Adress.adress + "DetectClusters2\\" + cluster
#     NIdV = snap.TIntV()
#     with open(resource, "r") as file:
#         for line in file:
#             NIdV.Add(int(line[0:-1]))
#     SubGraph = snap.GetSubGraph(Graph, NIdV)
#     DegToCCfV = snap.TFltPrV()
#     result = snap.GetClustCfAll(SubGraph, DegToCCfV)
#     # print("average clustering coefficient"+str(cluster), result[0])
#     if result[0]>0.1:
#         num+=1
#         for i in NIdV:
#             clusterNodes.add(i)
#
# #     print(len(clusterNodes))
# print(len(clusterNodes))
# print(str(num))

# ***************************************************************************************************************


# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
#
# closeness = dict()
# i=0
# j=0
# for NI in Graph.Nodes():
#     CloseCentr = snap.GetClosenessCentr(Graph,NI.GetId())
#     closeness[NI.GetId()] = CloseCentr
#     if j>1400 and CloseCentr>=0.23:
#         i+=1
#     j+=1
# print(i)
# # max = {k: v for k, v in sorted(closeness.items(), key=lambda x: x[1], reverse=True)}
# # print(max)
#
# i=0
# j=0
# Nodes = snap.TIntFltH()
# Edges = snap.TIntPrFltH()
# bet=dict()
# # snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
# snap.GetBetweennessCentr(Graph, Nodes, 1.0)
# for node in Nodes:
#     bet[node]= Nodes[node]
#     if j>1400 and Nodes[node]>=7568.82:
#         i+=1
#     j+=1
#
# print(i)

# max = {k: v for k, v in sorted(bet.items(), key=lambda x: x[1], reverse=True)}
# print(max)
# print(i/len(Nodes))




from ExtensionDir import ExtensionCores

# noClusteredSeed=extensionClusterWithSquareAndTringleChanged.clusterExtention(0.5,True)
# if len(noClusteredSeed)>0:
#     noClusteredSeed = extensionClusterWithSquareAndTringleChanged.clusterExtention2(noClusteredSeed, True)
#
# Merge.Merge("DetectClusters","MergeClusters")
# ExtensionCores.ExtensionCore("DetectClusters")
# ExtensionCores.ExtensionCore("MergeClusters")
# Merge.Merge("ExtensionCores","MergeClusters")
# Merge.Merge("MergeClusters","MergeClusters2")
# Merge.Merge("MergeClusters6","MergeClusters7")
# Merge.Merge("MergeClusters7","MergeClusters8")
# Merge.Merge("MergeClusters8","MergeClusters")
# Merge.Merge("MergeClusters","MergeClusters2")
# Merge.Merge("MergeClusters2","MergeClusters3")


# Merge.Merge("MergeClusters3","MergeClusters4")
# Merge.Merge("MergeClusters4","MergeClusters5")
# Merge.Merge("MergeClusters5","MergeClusters6")
# Merge.Merge("MergeClusters6","MergeClusters7")
# Merge.Merge("MergeClusters7","MergeClusters8")
# convertToName.ConvertToName("MergeClusters2")
# convertToName.ConvertToName("ExtensionCores")
# convertToName.ConvertToName("DetectClusters")
# Evaluate.Evaluate()

#
# from SelectSeed import SeedCoefficient
# from Other import OtherFunctions
# from ExtensionDir import ExtensionSeed
#
# Graph = snap.LoadEdgeListStr(snap.PUNGraph, Adress.adress + "DataSets\\DIP_ProteinName.txt", 0, 1)
# seeds=SeedCoefficient.seedCoefficient(Graph,0.5)
#
# folder=Adress.adress+"ExtensionCores"
# OtherFunctions.DeleteDirectory(folder)
#
# setSeed=set()
# for seed in seeds:
#     setSeed.add(seed)
#     ExtensionSeed.ExtensionSeed(setSeed,"ExtensionCores",0,seed)
#
# convertToName.ConvertToName("ExtensionCores")
# Evaluate.Evaluate()


# from  NewExtension import ExtensionWithFormula
#
# ExtensionWithFormula.clusterExtention(True)

# convertToName.ConvertToName("DetectClusters")
# Evaluate.Evaluate()



# Merge.Merge("DetectClusters","MergeClusters")
# convertToName.ConvertToName("MergeClusters")
# Evaluate.Evaluate()
#
# Merge.Merge("MergeClusters","MergeClusters2")
# convertToName.ConvertToName("MergeClusters2")
# Evaluate.Evaluate()






