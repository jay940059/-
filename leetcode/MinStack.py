class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = 2147483648 #先預設min為最大值
        

    def push(self, x: int) -> None:
    
        if x <= self.min: #如果輸入的值小於等於min
            self.items.append(self.min) #先加 min
            self.min = x 
        self.items.append(x)

    def pop(self) -> None:
        
        peak =  self.items.pop()
        if self.min == peak:
            self.min = self.items.pop()
    def top(self) -> int:
        
        return self.items[-1]

    def getMin(self) -> int:
        
        return self.min