import Adress
import os
# def Evaluate(bonacichNodes):

def Evaluate():
    bonacichNodes = os.listdir(Adress.adress + "NamedClusters")
    numAllNodesUsed=set()
    standardComplex = {}
    with open(Adress.adress+"\\DataSets\\cyc.txt", "r") as file:
    # with open(Adress.adress+"\DataSets\cyc2.txt", "r") as file:
    # with open(Adress.adress+"\DataSets\cyc3.txt", "r") as file:
    # with open(Adress.adress+"\DataSets\cyc_for_krogan2006_core.txt", "r") as file:

        i = 0
        for line in file:
            # if len(line.split())>2:
            standardComplex[i] = line
            i += 1

    print("standardComplex= %d"%len(standardComplex))
    w, h = len(standardComplex), len(bonacichNodes);
    NA = [[0 for x in range(w)] for y in range(h)]
    numPredictCluster = 0
    Mc=0
    for i in bonacichNodes:
        i=int(i[0:i.find("_")])
        moreThanTreshold = False
        predictComplex = set()
        name = Adress.adress+"NamedClusters\\"+str(i) + "_protein_name.txt"

        with open(name, "r") as file:
            for line in file:
                predictComplex.add(line)

        # if len(predictComplex)>2:
        j = 0
        for id in range(len(standardComplex)):
            num = 0
            for predictProtein in predictComplex:
                predictProtein = predictProtein[:-1]
                numAllNodesUsed.add(predictProtein)
                if str(predictProtein) in standardComplex[id]:
                    num = num + 1
            length = len(standardComplex[id].split())
            NA[numPredictCluster][j] = num * num / (len(predictComplex) * length)
            if(NA[numPredictCluster][j]>=0.2 and not moreThanTreshold):
                moreThanTreshold=True
                Mc+=1
            j = j + 1
        numPredictCluster += 1

    Precision=Mc/numPredictCluster
    print("Precision=%f"%Precision)


    Mco=0
    for j in range(len(standardComplex)):
        for i in range(numPredictCluster):
            if(NA[i][j]>=0.2):
                Mco+=1
                break
    Recall=Mco/len(standardComplex)
    print("Recall=%f" % Recall)



    if Precision+Recall!= 0:
        F_measure=(2*Precision*Recall)/(Precision+Recall)
    else:
        F_measure=0
    print("F_measure=%f" % F_measure)
    print("numClustersDetects= " + str((numPredictCluster)))
    print("numNodesDetects= " + str(len(numAllNodesUsed)))
    # print("coverage= "+ str((len(numAllNodesUsed)/4928)*100))
    print("coverage= "+ str((len(numAllNodesUsed)/2708)*100))

# Evaluate()