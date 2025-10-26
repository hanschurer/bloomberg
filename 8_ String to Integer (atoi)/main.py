class Solution:
    def myAtoi(self, s: str) -> int:  # convert string to 32-bit signed integer
        INT_MAX = 2**31 - 1 
        INT_MIN = -2**31 
        i = 0  
        n = len(s) 
        # 1) skip leading spaces
        while i < n and s[i] == ' ':  
            i += 1  
        # 2) optional sign
        sign = 1  
        if i < n and (s[i] == '+' or s[i] == '-'): 
            sign = -1 if s[i] == '-' else 1 
            i += 1  
        # 3) read digits and build number: do overflow check before multiplying/adding the next digit
        res = 0  
        while i < n and s[i].isdigit():  
            d = ord(s[i]) - ord('0')  
            # overflow check 
            if sign == 1 and (res > INT_MAX // 10 or (res == INT_MAX // 10 and d > 7)):  # or 第二种情况对应2147483647: res == 214,748,36), then res*10 equals 2,147,483,640. We can only add at most 7 to stay ≤ 2,147,483,647.
                return INT_MAX  
            if sign == -1 and (res > (-INT_MIN) // 10 or (res == (-INT_MIN) // 10 and d > 8)):  # would overflow negative
                return INT_MIN  
            res = res * 10 + d  # safe to push this digit
            i += 1  
        return res * sign  
    
# TC: O(n) — single pass over the string.
# SC: O(1) — constant extra space, independent of input size.
