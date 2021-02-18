import snap
import numpy as np
import matplotlib.pyplot as plt

def calcFeaturesNode(Node, Graph):
    """
    return: 1. the degree of v, i.e., deg(v);
            2. the number of edges in the egonet of v, where egonet of v is defined as the subgraph of G
            induced by v and its neighborhood;
            3. the number of edges that connect the egonet of v and the rest of the graph, i.e., the number
            of edges that enter or leave the egonet of v.
    """
    feature = snap.TIntV()
    
    feature_1 = Node.GetOutDeg()
    
    neighbor_list = list(Node.GetOutEdges())    
    NIdV = snap.TIntV()
    for item in neighbor_list:
        NIdV.Add(item)
    NIdV.Add(Node.GetId())
    SubGraph = snap.GetSubGraph(Graph, NIdV)   
    feature_2 = snap.CntUniqUndirEdges(SubGraph)
    
    Graph_copy = snap.ConvertGraph(type(Graph), Graph)  
    snap.DelNodes(Graph_copy, NIdV)
    feature_3 =  Graph.GetEdges() - snap.CntUniqUndirEdges(SubGraph) - snap.CntUniqUndirEdges(Graph_copy)
    
    feature.Add(feature_1)
    feature.Add(feature_2)
    feature.Add(feature_3)
    
    return feature

    # create a graph PNGraph
def cal_initial_feature(graph):
    v_mat = []
    for node in graph.Nodes():
        v_mat.append(calcFeaturesNode(node, graph))
    return np.array(v_mat)     

def CosineSimilarity(a, b):
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def FindNearestKBasic(NId, Graph, k):
    Vs = {}
    for NI in Graph.Nodes():
        Vs[NI.GetId()] = calcFeaturesNode(NI, Graph)
    
    dsts = []
    for NI in Graph.Nodes():
        if NI.GetId() == NId:
            continue
        d = CosineSimilarity(Vs[NId], Vs[NI.GetId()])
        dsts.append((d, NI.GetId(), Vs[NI.GetId()]))
    dsts = sorted(dsts, reverse=True)
    return dsts[:k]



G1 = snap.TUNGraph.New()
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)
G1.AddNode(4)
G1.AddNode(5)
G1.AddNode(6)
G1.AddNode(7)
G1.AddNode(8)
G1.AddNode(9)
    
G1.AddEdge(1,2)
G1.AddEdge(1,3)
G1.AddEdge(1,4)
G1.AddEdge(1,5)

G1.AddEdge(2,6)
G1.AddEdge(6,7)
G1.AddEdge(7,8)
G1.AddEdge(8,9)
G1.AddEdge(9,2)

NId=9
result = FindNearestKBasic(NId, G1, 5)
#print(*result, sep='\n')
[print(a) for a in result
