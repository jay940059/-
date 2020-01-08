class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #第一個迴圈只拿一個數字
            for j in range(i+1,len(nums)):#第二個迴圈拿所有數字跟第一個得做比較
                if nums[i]+nums[j]==target:
                    return [i,j]
