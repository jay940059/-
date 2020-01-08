class Solution:
    def reverse(self, x: int) -> int:
        if x<0: #如果x小於0
            x = str(-x)[::-1] #將x變為字串並且反轉
            if -int (x)<=-2147483651: #反轉後的負數小於-32bit就回傳0
                return 0
            return -int(x) #回傳轉過來的x並加負號
        else:
            x = str(x)[::-1]
            if int (x)>=2147483651: #反轉後的數大於32bit就傳0
                return 0
            return int(x)
