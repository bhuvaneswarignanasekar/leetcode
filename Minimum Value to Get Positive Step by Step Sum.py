def minStartValue(nums):
        start=0
        
        for i in nums:
            if i>0:
                start+=i
            else:
                if start<i:
                    start=i
                    break
                else:
                    break
        temp=start
        while True:
            for i in nums:
                temp+=i
                if temp<0:
                    break
            if temp>0:
                return temp
            temp=start
print(minStartValue([2,-3,1,-3,1]))