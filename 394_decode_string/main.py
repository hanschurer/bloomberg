class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, res = [], 0, ""

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((res, num))
                res, num = "", 0
            elif c == ']':
                pre_str, mul = stack.pop()
                res = pre_str + mul * res
            else:
                res+=c
        
        return res