import snap

def intro():
    # create a graph PNGraph
    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(2)
    G1.AddNode(3)
    
    G1.AddEdge(1,2)
    G1.AddEdge(2,1)
    G1.AddEdge(1,3)
    G1.AddEdge(1,1)

    # The number of nodes in the network
    Count = G1.GetNodes()
    print("The Number of Nodes in the Network is:", Count)

    # The number of nodes with a self-edge (self-loop) in the network
    Count = snap.CntSelfEdges(G1)
    print("The Number of Nodes with a Self Edge in the Network is:", Count)

    # The number of directed edges in the network
    Count = G1.GetEdges()-snap.CntSelfEdges(G1)
    print("The Number of Directed Edges in the Network is:", Count)

    # The number of undirected edges in the network
    Count = snap.CntUniqUndirEdges(G1)
    print("The Number of Undirected Edges in the Network is:", Count)

    # The number of reciprocated edges in the network,
    Count = snap.CntUniqBiDirEdges(G1)
    print("The Number of reciprocated Edges in the Network is:", Count)

    cntZeroOut = snap.CntOutDegNodes(G1, 0)
    cntZeroIn = snap.CntInDegNodes(G1, 0)
    print("zero out-degree : %d and zero in-degree : %d" % (cntZeroOut, cntZeroIn))
    
    Count_TenInDeg =0;
    Count_TenOutDeg =0;

    for NI in G1.Nodes():
        if  NI.GetOutDeg() > 10 :
            Count_TenOutDeg = Count_TenOutDeg + 1;
        if NI.GetInDeg() < 10 :
            Count_TenInDeg = Count_TenInDeg + 1;
    
    print("more than 10 out-degree : %d and fewer than 10 in-degree : %d" % (Count_TenOutDeg, Count_TenInDeg))

if __name__ == '__main__':
    intro()
