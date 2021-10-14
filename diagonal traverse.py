class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
        print(m,n)
        d=defaultdict(list)
        res=[]
        for r in range(m):
            for c in range(n):
                d[r+c].append(mat[r][c])
                
        for key in d:
            j=d[key]
            if key%2==0:
                j=j[::-1]
            res+=j
        return res