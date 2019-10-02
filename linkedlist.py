class MyLinkedList:

    def __init__(self):
        
        self.val = None #self指本身class
        self.next = None
        # self.的設定，代表你可以用class的屬性

    def get(self, index: int) -> int: #冒號後面是參數的注釋  ->是函數返回值得注釋
  
        if self.val == None:
            return -1 #遇到第一個return就跳出來
        if index == 0:
            return self.val
        p = self.next
        i = 1
        while p != None: #當p有東西
            if i == index: #使用者輸入(想要的位置)相等 i
                return p.val #回傳p.val
            p = p.next #使用者輸入不等於i
            i += 1 #i = i+1
        return -1

    def addAtHead(self, val: int) -> None: #1-2-3-4-5
        
        if self.val == None: #如果val是空的
            self.val = val  #val就等於輸入的
            return
        temp = self.val # temp = 1
        self.val = val #class的第一個=使用者輸入 x-2-3-4-5
        tempnode = self.next # tempnode = 2
        self.next = MyLinkedList() # 2 = 新的LinkedList
        self.next.val = temp # x-1       
        self.next.next = tempnode # x-1-2-3-4-5
        return

    def addAtTail(self, val: int) -> None: #1-2-3
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.val = val
            return
        p = self #p = 1
        while p.next != None: #p有next
            p = p.next #p = p的下一個
        p.next = MyLinkedList() #
        p.next.val = val #尾巴是使用者輸入的
        return


    def addAtIndex(self, index: int, val: int) -> None: #1-2-3-4-5
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        i = 0
        p = self #p是後面的list
        pre = p #pre 是前面的list
        if index <= 0:  #如果是負數，直接加在最前面
            self.addAtHead(val) 
            return
        while i < index: #如果i小於輸入的位置
            i += 1  #i就加一
            pre = p #pre = 1
            if p != None and p.val != None: #如果p不是空值且p的值也不是空的
                p = p.next #p = 2
            else:
                return #值超過就結束
        pre.next = MyLinkedList() #pre.next的下一個為新的linked list
        pre.next.val = val #prep.next的值為使用者輸入的值
        pre.next.next = p #
        return
            

    def deleteAtIndex(self, index: int) -> None: #1-2-3-4-5
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        p = self # p = 1
        if index < 0: 
            return
        if index == 0: #使用者要刪第一個
            if self.val == None: #如果沒有值
                return
            if self.next == None: #如果沒有下一個
                self = None
                return
            self.val = self.next.val #
            self.next = self.next.next 
        pre = p #pre 為前面的
        while i < index: #如果i 小於輸入的
            i += 1 # i就加1
            pre = p #pre = 1
            if pre == None:
                return
            p = p.next #p = 2
        if p != None: #當i = index 且 p有值
            pre.next = p.next #刪掉中間的
        else:
            pre.next = None
        return 
