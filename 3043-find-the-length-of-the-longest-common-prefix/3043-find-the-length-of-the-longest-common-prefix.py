class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        count=0
        prefix=set()

        for a in arr1:
            a=str(a)
            pre=""
            for ch in a:
                pre=pre+ch
                prefix.add(pre)
            
        for b in arr2:
            b=str(b)
            pr=""
            cnt=0
            for ch in b:
                pr+=ch
                if pr in prefix:
                    cnt+=1
            if cnt>count:
                count=cnt


        return count            