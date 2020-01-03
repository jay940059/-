#!/usr/bin/env python
# coding: utf-8

# In[162]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w):
        if g.graph == []:
            g.graph = g.graph_matrix
        g.graph[u][v] = w
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        dist = g.graph[s]
        for i in range(len(dist)):
            if dist[i] == 0:
                dist[i] = float('inf') #這代表無限大的意思
                #[x,4,x,x,x,x,x,8,x]
        finish = []
        while len(finish) != len(dist): #當list裡面沒有無限大
            dist[s] = float('inf') #把自己設為無限大
            Minlist = sorted(dist) #Minlist 是 dist 按照順序排好 Minlist = [4,8,x,x,x,x,x,x,x]
            Min = 0 #第一個是最小的
            for i in range(len(Minlist)-1): #如果已經在finish裡面就換下一個
                if Minlist[Min] in finish:
                    Min+=1

            MinVal = Minlist[Min] #MinVal = 4
            finish.append(MinVal)
            lista = g.graph[dist.index(MinVal)] #把lista調出來 lista = [4,0,8,0,0,0,0,11,0]
            lista = [i+MinVal for i in lista] #讓lista全部都加過在dist中min的值 lista = [8,4,12,4,4,4,4,15,4]

            for k in range(len(dist)):
                if lista[k] == MinVal:
                    continue
                if lista[k] < dist[k]:
                    dist[k] = lista[k]
            dist[s] = 0
        dicta = {str(i):dist[i] for i in range(0, len(dist))}

        return dicta
    
    def Kruskal(self):
        answer = []
        finish = []
        dicta = {}
        for i in g.graph:
            for a in i:
                if a != 0:
                    answer.append(a)
        answer.sort()
        for i in answer:
            for a in range(len(g.graph)-1):
                if i in g.graph[a]:
                    if g.graph[a].index(i):
                        if g.graph[a].index(i) in finish and a in finish:
                            break
                        else:
                            finish.append(a)
                            finish.append(g.graph[a].index(i))
                            dicta[str(a)+'-'+str(g.graph[a].index(i))]=i
        return(dicta)
                            
                            
                        
        


# 參考資料:https://www.youtube.com/watch?v=NLp9C7AvJhk
# http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html
