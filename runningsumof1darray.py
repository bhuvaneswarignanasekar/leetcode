class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        t_sum=sum(nums)
        res=[t_sum]
        for i in reversed(nums):
            t_sum-=i
            res.insert(0,t_sum)
        return res[1:]
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))
        return res