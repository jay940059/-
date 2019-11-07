class Solution(object):
    
    def Maxheap(self,data):
        for i in range(len(data)-1,-1,-1): #從最後一個開始
            if i%2 == 1 or i-1<=0: #如果是單數或是要最後一個就直接跳掉
                continue
            if data[i] > data[i-1]: #挑選哪一個子元素要跟父元素做比較
                Solution().Push(data,int(i/2)-1,i)
            else:
                Solution().Push(data,int(i/2)-1,i-1)
            
    
    def Push(self,data,x,y): #填入list,父元素位置，子元素位置
        if data[x] < data [y]: #如果父元素小於子元素就交換
            data[x],data[y] = data[y],data[x]
            Solution().Challenge(data,y) #交換完要看需不需要跟新的子元素交換
            return data
        else:
            return data
    
    def Challenge(self,data,x): #填入list,要被挑戰的父元素
        right = (x+1)*2 #右邊的子元素
        left = right -1 #左邊的子元素
        if len(data)-1<left: #假如左元素或右元素不存在直接回傳
            return data
        if len(data)-1>=right:
            if data[right]>data[left]: #如果右元素大於左元素，就去跟父元素做比較
                Solution().Push(data,x,right)
                return(data)
        Solution().Push(data,x,left) #左元素跟父元素做比較
        return(data)


    def heap_sort(self,data): 
        answer = [] #answer的list
        Solution().Maxheap(data) #先做 Max Heapify的動作
        while len(data) != 0: #只要list還有值就會繼續做
            Solution().Challenge(data,0) #看第一個是不是最大的
            data[0],data[-1] = data[-1],data[0] #把第一個值(最大的)跟最後一個做交換
            answer.insert(0,data[-1]) #把最大的加到answer
            data.pop(-1) #把最後一個去除掉
            print (answer)
        return answer


# In[14]:


output = Solution().heap_sort([250,200,150,7,10,16,-5,17,18,19,50,100,49,35,38,70,15])
output


# 參考網址 : https://www.youtube.com/watch?v=GnKHVXv_rlQ
