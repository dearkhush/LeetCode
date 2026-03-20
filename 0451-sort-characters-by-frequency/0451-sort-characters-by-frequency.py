class Solution:
    def frequencySort(self, s: str) -> str:
        l = []
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0)+1

        for k in freq:
            l.append((k,freq[k]))
        
        l.sort(key=lambda x: (-x[1], x[0]))

        res = ""

        for a,b in l:
            for i in range(b):
                res += a

        return res


        