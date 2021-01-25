import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1= collections.Counter(word1)
        c2=collections.Counter(word2)
        if sorted(c2.values()) == sorted(c1.values()) and c1.keys() == c2.keys():
            return 1
        else:
            return 0