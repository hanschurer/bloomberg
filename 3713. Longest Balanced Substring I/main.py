class Solution:
    def longestBalanced(self, s: str) -> int:
        '''
        TC: Outer loop n and inner loop ≤ n ⇒ O(n²).
                Each inner iteration scans 26 counts ⇒ constant factor (26) ⇒ overall O(n²).
        SC: Only the 26-element freq array and a few scalars ⇒ O(1).
        '''

        n = len(s)  
        best = 0  # track longest balanced substring length found so far
        for start in range(n):  # iterate over every possible starting index
            freq = [0] * 26  # initialize frequency array for 26 lowercase letters
            for end in range(start, n):  # extend the window one character at a time
                idx = ord(s[end]) - 97  # map character to array index 0-25
                freq[idx] += 1  # increment frequency of current letter
                if (end - start + 1) <= best:  # skip check without evaluating max_freq and min_freq if current window is already shorter than best
                    continue 
                min_f = 1001  
                max_f = 0  
                for f in freq: 
                    if f == 0:  # skip zero frequencies
                        continue  
                    if f < min_f:  # update minimum non-zero frequency
                        min_f = f  
                    if f > max_f:  # update maximum frequency
                        max_f = f  
                if min_f == max_f:  # balanced condition: all non-zero frequencies equal
                    best = end - start + 1  # update best with current window length
        return best  # return the longest balanced substring length
        


        