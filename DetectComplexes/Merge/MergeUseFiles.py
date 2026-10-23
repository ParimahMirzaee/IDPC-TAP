import Adress
import os

# در این جا ما همه را چک میکنیم بدون توجه به اینکه آیا قبلا ادغام شده است یا نه؟
def Merge(callAgain,exist):
    #callAhain : اگر یک باشد یعنی بازگشتی نبوده است+
    while exist:
        j=0
        clusters = os.listdir(Adress.adress + "DetectClusters")
        print("num Clusters before merge: "+str(len(clusters)))
        #exist: نشان می دهد که حتما دو فایل بوده اند که ادغام شوند اگر فالس باشد یعنی ادغامی صورت نگرفته است.
        exist=False
        max = 0
        maxId = 0
        for id in clusters:
            listNodesName = set()
            name =Adress.adress+"DetectClusters\\" + id
            #خواندن نودهای یک کلاستر
            with open(name, "r")as f:
                for line in enumerate(f):
                    for i in line[1].split():
                        listNodesName.add(i)
            max=0
            maxId=0
            #خواندن نودهای کلاستر های دیگر به جز کلاستر اصلی
            for another in clusters:
                if id != another:
                    listNodesNameOthers = set()
                    name = Adress.adress+"DetectClusters\\" + another
                    with open(name, "r")as f:
                        for line in enumerate(f):
                            for i in line[1].split():
                                listNodesNameOthers.add(i)

                    intersect=list(set(listNodesName) & set(listNodesNameOthers))
                    if len(listNodesName)==0 or len(listNodesNameOthers)==0:
                        a=3
                    rate=len(intersect)/min(len(listNodesName),len(listNodesNameOthers))
                    if rate > max:
                        max = rate
                        maxId = another

            if max>0.5:
                if(j==391):
                    a=2
                j += 1
                exist=True
                nameNewFile = Adress.adress + "DetectClusters\\" + "merge" + str(callAgain)+"-"+str(j) + ".txt"
                print(nameNewFile)
                newFile=open(nameNewFile,"w")
                name =Adress.adress+"DetectClusters\\" + id
                with open(name, "r")as f:
                    for line in enumerate(f):
                        a,b=line[1].split()
                        # addToFile(str(i)+str(j),a+"	"+b+"\n")
                        newFile.write(a+"	"+b+"\n")
                name =Adress.adress+"DetectClusters\\" + maxId
                with open(name, "r")as f:
                    for line in enumerate(f):
                        a,b=line[1].split()
                        if(not isEdge(a,b,id)):
                            newFile.write(a+"   "+b + "\n")
                newFile.close()
                os.remove(Adress.adress + "DetectClusters\\" + id)
                os.remove(Adress.adress + "DetectClusters\\" + maxId)
                clusters.remove(id)
                clusters.remove(maxId)
        callAgain += 1
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

