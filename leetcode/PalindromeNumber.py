class Solution:
    def isPalindrome(self,x):
        if x<0: #如果是負數就不會是倒數
            return(False)
        else:
            if str(x) == str(x)[::-1]: #如果是正數倒數就會跟自己相等
                return(True)
            else:
                return(False)
