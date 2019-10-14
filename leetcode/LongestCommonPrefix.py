class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: #如果是空字串回傳0
            return ''
        res = '' # 設res為空字串
        for i in range(len(strs[0])): #總共跑第一個字串的字數
            for j in range(1, len(strs)): #從第二個字串開始比較
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]: #如果全部都比完了或字串裡的字跟第一個的字串內容不一樣時
                    return res
            res += strs[0][i]
        return res