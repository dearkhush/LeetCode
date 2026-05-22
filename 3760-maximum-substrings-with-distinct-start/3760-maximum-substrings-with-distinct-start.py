class Solution:
    def maxDistinct(self, s: str) -> int:
        count=0
        s=set(s)
        for elem in s:
            count+=1
        return count