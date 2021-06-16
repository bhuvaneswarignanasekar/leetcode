class NumArray:
    num=[]
    def __init__(self, nums: List[int]):
        self.num=nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.num[left:right+1])
