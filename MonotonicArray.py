class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pre=nums[0]
        flag=0
        for it in nums:
            if it>=pre:
                pass
            else:
                flag=1
                break
            pre=it
        if flag==0:return True
        pre=nums[0]
        for it in nums:
            if it<=pre:
                pass
            else:
                return False
            pre=it
        return True