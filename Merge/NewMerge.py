import Adress
import os

# در این جا ما همه را چک میکنیم بدون توجه به اینکه آیا قبلا ادغام شده است یا نه؟
def Merge(callAgain):
    #callAhain : اگر یک باشد یعنی بازگشتی نبوده است
    print(str(callAgain))
    j=0
    clusters = os.listdir(Adress.adress + "DetectClusters")
    mergedFiles=set()
    print("num Clusters before merge: "+str(len(clusters)))
    #exist: نشان می دهد که حتما دو فایل بوده اند که ادغام شوند اگر فالس باشد یعنی ادغامی صورت نگرفته است.
    exist=False
    for id in clusters:
        listNodesName = set()
        name =Adress.adress+"DetectClusters\\" + id
        with open(name, "r")as f:
            for line in enumerate(f):
                for i in line[1].split():
                    listNodesName.add(i)
            for another in clusters:
                if id != another:
                    listNodesNameOthers = set()
                    name = Adress.adress+"DetectClusters\\" + another
                    with open(name, "r")as f:
                        for line in enumerate(f):
                            for i in line[1].split():
                                listNodesNameOthers.add(i)

                    intersect=list(set(listNodesName) & set(listNodesNameOthers))
                    rate=len(intersect)/min(len(listNodesName),len(listNodesNameOthers))
                    if rate>0.5:
                        exist=True
                        mergedFiles.add(id)
                        mergedFiles.add(another)
                        j += 1
                        nameNewFile = Adress.adress + "DetectClusters\\" + "merge" + str(callAgain)+"-"+str(j) + ".txt"
                        print(nameNewFile)
                        newFile=open(nameNewFile,"w")
                        name =Adress.adress+"DetectClusters\\" + id
                        with open(name, "r")as f:
                            for line in enumerate(f):
                                a,b=line[1].split()
                                # addToFile(str(i)+str(j),a+"	"+b+"\n")
                                newFile.write(a+"	"+b+"\n")
                        name =Adress.adress+"DetectClusters\\" + another
                        with open(name, "r")as f:
                            for line in enumerate(f):
                                a,b=line[1].split()
                                if(not isEdge(a,b,id)):
                                    newFile.write(a + "	" + b + "\n")
                                    # addToFile(str(i)+str(j),a+"	"+b+"\n")

    #فایل هایی که ادغام شده اند را در آخر حذف می‌کند
    for id in mergedFiles:
        os.remove(Adress.adress+"DetectClusters\\" + id)
    if(exist):
        Merge(callAgain+1)
#*************************************************************************************************

def isEdge(node1 , node2, id):
    name=Adress.adress+"DetectClusters\\" +id
    x=node1+"	"+node2
    x1=node2+"	"+node1

    with open(name) as f:
        f.readline()
        f.readline()
        f.readline()
        if x in f.read():
            return True
        elif x1 in f.read():
            return True
        else:
            return False
#**************************************************************************************************

# def addToFile(id,x):
#     name = Adress.adress + "DetectClusters\\" + "merge" + str(i) + str(j) + ".txt"
#     with open(name, "a") as myfile:
#         myfile.write(x)

#***************************************************************************************************

def deleteThreeLine(name):
    f = open(name, 'r')
    linelist = f.readlines()
    f.close

    # Re-open file here
    f2 = open(name, 'w')
    f2.writelines(linelist[3: ])
    f2.close()