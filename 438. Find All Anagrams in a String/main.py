class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        res = []
        l = 0
        for r, c in enumerate(s):
            counter[c]-=1

            while  counter[c] <0:
                counter[s[l]]+=1
                l+=1
            
            if r-l+1 == len(p):
                res.append(l)
        
        return res