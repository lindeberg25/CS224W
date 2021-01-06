import snap
from matplotlib import pyplot
import numpy as np
import pandas as pd

def intro():
    
    # 1 Analyzing the Wikipedia voters network
    
    # create a graph PNGraph
    G1 = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 0, 1)

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

    # 2 - Further Analyzing the Wikipedia voters network

    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(G1, DegToCntV)
    x=[]
    y=[]
    for item in DegToCntV:
        if item.GetVal1()>0:
            x.append(np.log10(item.GetVal1()))
            y.append(np.log10(item.GetVal2()))
    
    a,b = np.polyfit(x, y, 1)
    pyplot.plot(x,y)
    pyplot.xlabel('Out-deegree')
    pyplot.ylabel('Number of Nodes')
    pyplot.title('Distribution of out-degrees')

    x2=np.linspace(min(x),max(y),100)
    pyplot.plot(x2,a*x2+b)
    pyplot.legend(['Data line','Regression line'])
    #pyplot.show()

# Finding Experts on the Java Programming Language on StackOverFlow

    # create a graph PNGraph
    G2 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
    
    # The number of weakly connected components in the network.
    Components = snap.TCnComV()
    snap.GetWccs(G2, Components)
    print("The number of weakly connected components is %d" %  (Components.Len()))

    # The number of edges and the number of nodes in the largest weakly connected component.
    MxWcc = snap.GetMxWcc(G2)
        
    print("Largest weakly connected component has %d edges and %d nodes" % (MxWcc.GetEdges(), MxWcc.GetNodes()))

    # IDs of the top 3 most central nodes in the network by PagePank scores.
    PRankH = snap.TIntFltH()
    snap.GetPageRank(G2, PRankH)

    pr_list=[]
    for item in PRankH:
        pr_list.append([item, PRankH[item]])

    pr=pd.DataFrame(pr_list,columns=['Node','PageRank']).sort_values(by='PageRank',ascending=0)

    print(pr[0:3])

    # IDs of the top 3 hubs and top 3 authorities in the network by HITS scores.
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(G2, NIdHubH, NIdAuthH)
    hubs_list=[]
    aths_list=[]
    for item in NIdHubH:
        hubs_list.append([item, NIdHubH[item]])
    for item in NIdAuthH:
        aths_list.append([item, NIdAuthH[item]])

    hubs=pd.DataFrame(hubs_list,columns=['Node','HITS']).sort_values(by='HITS',ascending=0)
    aths=pd.DataFrame(aths_list,columns=['Node','HITS']).sort_values(by='HITS',ascending=0)

    print(hubs[:3])
    print(aths[:3])

if __name__ == '__main__':
    intro()
