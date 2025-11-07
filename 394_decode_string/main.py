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
    
    # follow-up in phone screen: Time complexity and Space complexity
    #               Interviewer keep asking about the space complexity in some edge cases
    #                              O(n): he asked does n mean the input size or have other meaning


    # using a list to store the current string, then join at the end
    def decodeString2(self, s: str) -> str:
        st, curr, num = [], [], 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                st.append((num, curr))
                num = 0
                curr = []
            elif c == ']':
                cur_num, prev_s = st.pop()
                curr = prev_s + cur_num * curr
            else:
                curr.append(c)
        return ''.join(curr)
    
