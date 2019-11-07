class Solution(object):
    
    def Merge(self,left,right): #要填入兩個List
        if len(left) == 0 and len(right) == 0: #如果兩個list都已經是空值了就直接回傳
            return
        if len(left) ==0: #如果左邊的list是0，就直接回傳右邊
            return right
        if len(right) == 0: #如果右邊的List是0，就直接回傳左邊
            return left
        if left[0]>right[0]: #如果左邊的第一個值大於右邊的值，就抓右邊的第一個並且變成list的值，再繼續Merge下去
            return ([right[0]] + Solution().Merge(left,right[1:])) 
        else:
            return ([left[0]] + Solution().Merge(left[1:],right)) #相反過來
    
    def merge_sort(self,data): 
        if len(data) == 1: #如果list只有一個的時候就直接回傳data
            return data
        half = int(len(data)/2) #List的一半
        left = data[0:half] #left是List左邊的區域
        right = data[half:len(data)] #Right就是右邊
        LeftPart = Solution().merge_sort(left) #繼續分割左邊的區域
        RightPart = Solution().merge_sort(right) #繼續分割右邊的區域
        return Solution().Merge(LeftPart,RightPart) #合併兩個



output = Solution().merge_sort([250,200,150,7,10,16,-5,17,18,19,50,100,49,35,38,70,15])
print(output)


