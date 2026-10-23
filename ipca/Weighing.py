import snap
import Adress

#count of common neighbors
def weighingEgdeNum(Graph):
    with open(Adress.adress+"DataSets\dip_output_protein_name.txt", "r") as file:
        listCmnNeighbors=list()
        # i=0
        for line in file:
            cmnNodes=""
            split=line.split()
            cmnNodes=split[0]+" "+split[1]+" : "
            cmnNodes+=str(snap.GetCmnNbrs(Graph,int(split[0]),int(split[1])))

            listCmnNeighbors.append(cmnNodes+"\n")
            # i+=1
            # if i==20:
            #     break
    file = open(Adress.adress+"DataSets\EdgeWeight.txt", "w")
    for cmn in listCmnNeighbors:
        file.write(cmn)
    file.close()

# weight of node: sum of weight of edge incident of node
#node : weight degree
def weightNodes(Graph):
    #get nodes
    file=open(Adress.adress + "DataSets\\dip_output_protein_name.txt","r")
    setNodes=set()
    for line in file.readlines():
        setNodes.add(int(line.split()[0]))
        setNodes.add(int(line.split()[1]))

    #weight of each edge
    dictWeightEdges=dict()
    file=open(Adress.adress + "DataSets\\EdgeWeight.txt","r")
    for line in file.readlines():
        dictWeightEdges[line.split()[0]+" "+line.split()[1]]=line.split()[3]

    #calculate weight of each node and save it
    file = open(Adress.adress + "DataSets\\NodesWeight.txt", "w")
    for node in setNodes:
        degree=0
        weightNode=0
        NodeVec = snap.TIntV()
        snap.GetNodesAtHop(Graph, node, 1, NodeVec, False)

        for neighbor in NodeVec:
            if str(node) +" "+ str(neighbor) in dictWeightEdges:
                weightNode+=int(dictWeightEdges[str(node) +" "+ str(neighbor)])
            elif str(neighbor) +" "+ str(node) in dictWeightEdges:
                weightNode+=int(dictWeightEdges[str(neighbor) +" "+ str(node)])

        degree=len(NodeVec)
        file.write(str(node)+ " : "+ str(weightNode)+" "+ str(degree)+"\n")
    file.close()


#مرتب سازی بر اساس وزن و بعد درجه
def ordernodes():
    dictNodeWeightDegree=dict() # node : weight , degree
    file=open(Adress.adress+"DataSets\\NodesWeight.txt","r")
    for line in file.readlines():
        dictNodeWeightDegree.setdefault((int(line.split()[0])),[])
        dictNodeWeightDegree[int(line.split()[0])].append(int(line.split()[2]))
        dictNodeWeightDegree[int(line.split()[0])].append(int(line.split()[3]))


    #مرتب شده بر اساس وزن نوده ها اگر وزن ها یکی بود بر اساس درجه نودها
    r = dict(sorted(dictNodeWeightDegree.items(), key=lambda x: (x[1][0], x[1][1]),reverse=True))
    # r = dict(sorted(dictNodeWeightDegree.items(), key=lambda x: (x[1][1]),reverse=True))
    print(r)
    l=list(r.keys())

    return l

#select seed
def weightingNodes(Graph):
    weighingEgdeNum(Graph)
    weightNodes(Graph)
    l=ordernodes()
    return l
#name of common neighbors
def weighingEgdeName(Graph):
    with open(Adress.adress+"DataSets\dip_output_protein_name.txt", "r") as file:
        i = 0
        setcmnNeighbors=list()
        for line in file:
            cmnNodes=""
            split=line.split()
            Nbrs = snap.TIntV()
            snap.GetCmnNbrs(Graph,int(split[0]),int(split[1]), Nbrs)
            cmnNodes+=split[0]+" "+ split[1]+" : "
            if len(Nbrs)==0:
                cmnNodes += "0 \n"
            else:
                for NId in Nbrs:
                    # print(i)
                    # print("node: %d" % NId)
                    cmnNodes += str(NId) + " "
                cmnNodes += "\n"

            setcmnNeighbors.append(cmnNodes)
            # i+=1
            # if i==70:
            #     break
    file = open(Adress.adress+"DataSets\EdgeWeight.txt", "w")
    for cmn in setcmnNeighbors:
        file.write(cmn)
    file.close()


def repeatedEdges():
    setEdges=set()
    file = open(Adress.adress+"DataSets\Eip_output_protein_name.txt", "r")
    setEdges=file.readlines()
    file.close()

    for line in setEdges:
        nodes=line.split()
        if nodes[1]+" "+nodes[0]+" \n" in setEdges:
            print(line)