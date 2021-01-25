class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=len(mat)
        col=len(mat[0])
        diagonal=defaultdict(list)
        for i in range(rows):
            for j in range(col):
                diagonal[i-j].append(mat[i][j])
        
        for i in diagonal.keys():
            diagonal[i]=sorted(diagonal[i])
        
        for i in range(rows):
            for j in range(col):
                a=diagonal[i-j]
                mat[i][j]=a[0]
                a.pop(0)
        
        
        return mat