import snap
def clusterCoefficient(graph):
    DegToCCfV = snap.TFltPrV()
    result = snap.GetClustCfAll(graph, DegToCCfV)
    # for item in DegToCCfV:
    #     print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    # print("average clustering coefficient", result[0])
    # print("closed triads", result[1])
    # print("open triads", result[2])
    return result[0]