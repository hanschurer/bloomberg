class Solution: 
    def nextBeautifulNumber(self, n: int) -> int:  
        # helper也可以改为直接用counter
        '''
        TC: In the worst case we may scan a few thousand numbers after n; for each we count at most 7 digits ⇒ ≈ O((1224444-n) × 7) which is well within O(10 000) for the given constraints (practically constant).  
        Space: O(1) — only a fixed-size array of 10 counts irrespective of n.
        '''
        def is_balanced(x: int) -> bool:  # helper to test if x is numerically balanced
            counts = [0] * 10  
            while x:  
                d = x % 10  # extract last digit
                if d == 0:  # digit 0 can never satisfy "appears 0 times" if it appears at all
                    return False  
                counts[d] += 1 
                x //= 10  # drop the last digit
            for d in range(1, 10): 
                if counts[d] and counts[d] != d: 
                    return False  # then x is not balanced
            return True 
        candidate = n + 1  # first number strictly greater than n
        while not is_balanced(candidate):  # loop until we find a balanced number
            candidate += 1  
        return candidate  
    
    def nextBeautifulNumber2(self, n: int) -> int:
        from collections import Counter
        '''
        Given the range 0≤n≤10^6, the maximum numerically balanced number we may need to consider is C=1224444, 
        this range can be explored within acceptable time limits.

        TC: O(C−n), C=1224444
        SC: O(1).
        '''
        for i in range(n + 1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i
            
    