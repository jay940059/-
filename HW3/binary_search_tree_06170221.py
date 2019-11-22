#!/usr/bin/env python
# coding: utf-8

# In[191]:



class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
    def PrintTree(self): #把tree整個印出來
        if self.left:
            self.left.PrintTree()#先印最小的
        print(self.val)#印root
        if self.right:
            self.right.PrintTree()#在印大的
            

            
class Solution(object):
    
    def insert(self, root, val): #增加
        
        if root is not None: #如果有root
            if val > root.val: #輸入的值大於 root
                if root.right is None: #如果右邊沒有東西
                    root.right = TreeNode(val) #給予她右邊的值
                    return(root.right) #回傳值
                else: #如果右邊有東西
                    root = root.right #繼續尋找
                    return(Solution().insert(root,val))
            if val <= root.val: #左邊也是一樣的概念
                if root.left is None:
                    root.left = TreeNode(val)
                    return(root.left)
                else:
                    root = root.left
                    return(Solution().insert(root,val))
                
        else:
            root = TreeNode(val) #如果原本就沒東西直接變root
            return root
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
    def delete(self, root, target):
        a = Solution().search(root,target)
        while a is not None: #如果搜尋的到就繼續做
        
            if root is None: #如果root沒東西就直接回傳
                return root
        
            if root.val > target : #如果輸入值小於root
                root.left = Solution().delete(root.left,target) #繼續從左邊繼續找
        
            elif  root.val < target : #如果輸入值大於root
                root.right = Solution().delete(root.right,target) #繼續從右邊繼續找
        
            else: #當找到值的時候
                if root.left is None : #如果左邊是None
                    temp = root.right 
                    root = None #刪掉root值
                    return temp #回傳temp值
            
                if root.right is None :
                    temp = root.left
                    root = None
                    return temp
        
                change = Solution().SmallNode(root.right) #要交換的值就是右邊最小的
                root.val = change.val #交換值
                root.right = Solution().delete(root.right,change.val) #刪掉剛剛交換的值
            a = Solution().search(root,target)
        return root
            
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self, root, target):
        
        if root is None: #如果root是None直接回傳
            return 
        
        elif root.val > target: #如果輸入的值小於root
            root = root.left #從左邊繼續尋找
            return Solution().search(root,target)
        
        elif root.val < target: #如果輸入的值大於root
            root = root.right #從右邊繼續尋找
            return Solution().search(root,target)
        
        elif root.val == target: #如果想等就回傳
            return root
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
    def modify(self, root, target, new_val):
        count = 0 #假設一個變數為 0
        temp = Solution().search(root,target) #temp為target的位置
        while temp is not None and temp.val == target: #如果等於target，count的值就 +1
            count += 1
            temp = temp.left #繼續從左邊找
            
        Solution().delete(root,target) #把全部都刪掉
        
        for i in range(count): #加上被刪掉的值
            Solution().insert(root,new_val)
        return root
            
        
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def SmallNode(self,root): #計算最小的功能
        
        small = root
        if small.left is not None: #一直從左邊尋找
            small = small.left
            return(Solution().SmallNode(small))
        return small
        


# 參考資料 <br/>
# https://emn178.pixnet.net/blog/post/95499086 <br/>
# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm <br/>
# http://codepad.org/BSZDnLJ4 <br/>
# http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html#delete <br/>
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/ <br/>
