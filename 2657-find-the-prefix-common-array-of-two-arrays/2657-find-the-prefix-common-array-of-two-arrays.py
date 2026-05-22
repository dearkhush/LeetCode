class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l=[]
        c=[]
        for i in range(len(A)):
            count=0
            l.append(A[i])
            for j in range(i+1):
                if B[j] in l:
                    count+=1
            c.append(count)
        return c
                