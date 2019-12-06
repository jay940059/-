#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity #1~5個格子
        self.data = [None] * capacity #建立5個空的ListNode
        
        
    def code(self,key): #轉換成MD5
        h = MD5.new()
        key = str(key)
        h.update(key.encode("utf-8")) 
        key = int(h.hexdigest(),16)
        return(key)
        
        
    def add(self, key): #增加
        code = MyHashSet().code(key) # 將輸入的轉成MD5
        bucketcode = code % self.capacity #看要放進哪一個格子
        cur = self.data[bucketcode] 
        if cur is None: #如果這個格子沒有這個東西，就直接建立一個ListNode
            self.data[bucketcode] = ListNode(code)
            return
        while cur: #只要有cur
            if cur.next is None: #如果下一個沒有東西，就建立下一個
                cur.next = ListNode(code) 
                return
            else:
                cur = cur.next #繼續往下一個找
                
        
    def remove(self, key): #移除
        code = MyHashSet().code(key) #將輸入的轉成MD5
        bucketcode = code % self.capacity
        cur = self.data[bucketcode]
        while self.contains(key) is False: #如果沒有了輸入的數字直接回傳
            return
        if cur.val == code: #如果第一個就是要刪除的數
            self.data[bucketcode] = cur.next #將下一個指認為頭
            self.remove(key) #繼續尋找有沒有別的
            return 
        while cur.next: #如果有下一個
            if cur.next.val == code: #如果下一個是要刪除的數
                cur.next = cur.next.next #刪除中間的
                self.remove(key) #繼續尋找
                return 
       
        
    def contains(self, key):
        code =  MyHashSet().code(key)
        bucketcode = code % self.capacity
        cur = self.data[bucketcode]
        while cur: #如果有cur
            if cur.val == code: #如果相等輸入的值
                return True #回傳True
            cur = cur.next #或是繼續往下找
        return False #沒找到就return False
    
    
    


# 參考網址: https://leetcode.com/problems/design-hashset/discuss/279957/Python-Chaining
