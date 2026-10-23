import snap
from heapq import nlargest

# برگرداندن درجه نودهای گراف
def allDegreeNodesGraph(Graph):
    InDegV = snap.TIntPrV()
    snap.GetNodeInDegV(Graph, InDegV)
    dictDegreeDip = {}
    for item in InDegV:
        # print("node ID %d: in-degree %d" % (item.GetVal1(), item.GetVal2()))
        dictDegreeDip[item.GetVal1()] = item.GetVal2()
    return dictDegreeDip



# برگرداندن درجه یک نود خاص
def getDegreeSpecificNode(i,degreeNodesPickle):
    return (int(degreeNodesPickle[i]))


# برگزداندن درجه نودها به ترتیب بزرگ به کوچک
def largestDegrees(dictDegreeDip,clusterNodes,n):
    for i in range(len(clusterNodes)):
        dictDegreeDip.pop(list(clusterNodes)[i])
        #n:تعداد عددی ک برای خروجی می خواهیم
    max = nlargest(n, dictDegreeDip, key=dictDegreeDip.get)
    return max

    # use this
    # for i in range(5):
    #     print(max[i])


