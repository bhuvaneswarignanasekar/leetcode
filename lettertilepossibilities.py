from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        al_per=[]
        for i in range(1,len(tiles)+1,1):
            per=permutations(tiles,i)
            for j in per:al_per.append(j)
        return len(set(al_per))
                