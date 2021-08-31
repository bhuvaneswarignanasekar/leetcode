class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic={}
        count=1
        res=[]
        s_arr=sorted(arr)
        for i in s_arr:
            if i not in dic:
                dic[i]=count
                count+=1
        for i in arr:
            res.append(dic.get(i))
        return res
        