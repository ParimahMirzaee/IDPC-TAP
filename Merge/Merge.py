import Adress
import os
from Other import OtherFunctions
from PickleData import convertToName
from Evaluate import Evaluate

# folderRes ="OtherDataSet\\detect_krogen_core"
# folderDes = "MergeClusters"

# folderRes = "MergeClusters"
# folderDes = "MergeClusters2"

# folderRes = "MergeClusters2"
# folderDes = "MergeClusters3"

folderRes = "MergeClusters3"
folderDes = "MergeClusters4"
#
# folderRes = "MergeClusters4"
# folderDes = "MergeClusters5"
#
# folderRes = "MergeClusters5"
# folderDes = "MergeClusters6"

# def Merge(clusters):
def Merge(folderRes,folderDes):


    #حذف فایل‌های مرج شده قبلی
    folder = Adress.adress + folderDes
    OtherFunctions.DeleteDirectory(folder)


    dictMerged=dict()
    numClusters=0

    clusters = os.listdir(Adress.adress + folderRes)
    aset=set()
    for id in clusters:
        name = Adress.adress + folderRes+"\\" + id
        with open(name, "r")as f:
            for line in enumerate(f):
                # a, b = line[1].split()
                aset.add(line[1])
                # aset.add(b)
    print("num nodes before merge= "+str(len(aset)))
    # nonZero=set()
    print("num Clusters before merge: " + str(len(clusters)))

    for id in clusters:
        setNodesName = set()
        # name=Adress.adress+"DetectClusters\\" + str(id) + ".txt"
        name=Adress.adress+ folderRes+"\\"  + id
        with open(name, "r")as f:
            for line in enumerate(f):
                # for i in line[1].split():
                setNodesName.add(line[1])
        max=0
        maxId=0
        for another in clusters:
            if id != another :
                setNodesNameOthers = set()
                name = Adress.adress+ folderRes+"\\"  + another
                with open(name, "r")as f:
                    for line in enumerate(f):
                        # for i in line[1].split():
                        setNodesNameOthers.add(line[1])
                intersect=list(set(setNodesName) & set(setNodesNameOthers))
                rate=len(intersect)/min(len(setNodesName),len(setNodesNameOthers))
                if rate>max:
                    max=rate
                    maxId=another

        if max>0.9:
            exist=False
            #چک می کند آیا قبلا این کلاستر تولید شده است یا نه؟
            for id2, maxId2 in dictMerged.items():
                if maxId2 == id and maxId == id2:
                    # print(str(id) + "==" + str(maxId))
                    exist=True
            if not exist:
                numClusters += 1
                dictMerged[id]=maxId
                # clusters.remove(maxId)
                # clusters.remove(id)
                name = Adress.adress +  folderRes+"\\" + id
                with open(name, "r")as f:
                    for line in enumerate(f):
                        # a, b = line[1].split()
                        # addToFile(folderDes +"\\" +str(id[0:-4]),a+"	"+b+"\n")
                        addToFile(folderDes +"\\" +str(id[0:-4]),line[1])

                #add edge for merge ***********************************************************
                # name =Adress.adress+ folderRes+"\\"  + maxId
                # with open(name, "r")as f:
                #     for line in enumerate(f):
                #         a,b=line[1].split()
                #         if(not isEdge(a,b,folderRes +"\\" +id)):
                #             addToFile(folderDes +"\\" +str(id[0:-4]),a+"	"+b+"\n")

                # add node for merge ***********************************************************
                name = Adress.adress + folderRes + "\\" + maxId
                with open(name, "r")as f:
                    for line in enumerate(f):
                        # a, b = line[1].split()
                        if (line[1] not in setNodesName):
                            addToFile(folderDes + "\\" + str(id[0:-4]),line[1] )
                        # elif (b not in setNodesName):
                        #     addToFile(folderDes + "\\" + str(id[0:-4]),b + "\n")

                #********************************************************************************


            # nonZero.add(maxId)
        else:
            numClusters+=1
            # clusters.remove(id)
            from shutil import copyfile
            # print("**"+str(id))
            copyfile(Adress.adress+folderRes+"\\" + id, Adress.adress+folderDes+"\\"+ id)
        # print("num= "+str(len(num)))

    # for id, maxId in dictMeged.items():
    #     print(str(id) + "->" + str(maxId))


    clusters = os.listdir(Adress.adress + folderDes)
    aset=set()
    for id in clusters:
        name = Adress.adress + folderDes+"\\" + id
        with open(name, "r")as f:
            for line in enumerate(f):
                # a, b = line[1].split()
                aset.add(line[1])
                # aset.add(b)
    print("num nodes after merge= " + str(len(aset)))
    print("num Clusters after merge= "+str(numClusters))




    # print(len(nonZero))
    # return nonZero

def isEdge(node1 , node2, id):
    name=Adress.adress+ id
    x=node1+"	"+node2
    x1=node2+"	"+node1

    with open(name) as f:
        if x in f.read():
            return True
        elif x1 in f.read():
            return True
        else:
            return False


def addToFile(id,x):
    name=Adress.adress+id+".txt"
    with open(name, "a") as myfile:
        myfile.write(x)



Merge(folderRes,folderDes)

# convertToName.ConvertToName("MergeClusters")
# Evaluate.Evaluate()