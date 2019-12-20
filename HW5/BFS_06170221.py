#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s):
        num = s #設定一個num變數
        answer = [] #裝答案的list
        queue = [] #裝還未尋訪的list
        queue.append(num)
        while len(queue) != 0: #如果queue的長度不是0就繼續做下去
            
            for i in self.graph[num]: #把有連接到num的數都印出來
                if i not in answer and i != num: #如果數有在answer或是等於目前在使用的數就不加進queue
                    queue.append(i)
            if queue[0] not in answer:        
                answer.append(queue[0]) #答案加上queue的第一個數
            
            del queue[0] #並且刪掉
            if len(queue) != 0: #如果queue長度不等於0
                num = queue[0] #設定num變數為新的queue的第一個
            else:
                return answer  #如果queue長度是0的話，代表已經尋訪完畢直接回傳
        return answer            
        
        
    def DFS(self, s):

        answer = [] #放answer的list
        stack = [] #堆疊的list
        stack.append(s) #把輸入的數加進堆疊中
        while len(stack) != 0: #如果堆疊的長度不為0就繼續做
            a = stack.pop() #設定一個變數a為stack的最後一個
            answer.append(a) #並且加到answer裡面
            for i in self.graph[a]: #把跟a有聯繫的數字加進堆疊裡面
                if i not in answer: #如果有在answer裡面的就不加進去
                    stack.append(i) 
            if len(stack) == 0: #如果堆疊被掏空了
                    return answer #就回傳
  


# 參考資料: https://www.youtube.com/watch?v=bD8RT0ub--0
