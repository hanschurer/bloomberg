from typing import List  
class Solution: 
    def evalRPN(self, tokens: List[str]) -> int: 
        stack: List[int] = []  # stack to hold intermediate integer results
        for tok in tokens:  
            if tok in {"+", "-", "*", "/"}:    # pop left/right operand if the token is an operator
                b = stack.pop() 
                a = stack.pop() 
                if tok == "+": 
                    stack.append(a + b)  
                elif tok == "-":  
                    stack.append(a - b) 
                elif tok == "*": 
                    stack.append(a * b) 
                else:  
                    stack.append(int(a / b))  # use int(a / b) to truncate toward zero (not floor): drop the fractional part in the direction of zero—make it less positive if positive, or less negative if negative.
            else:  # token is a number
                stack.append(int(tok))  # convert string to integer and push
        return stack[-1]  # final result is the only value remaining on the stack
    
# Time: O(n) — each token is processed once; each push/pop is O(1).
# Space: O(n) — worst case: all numbers before any operator, the stack can hold up to n integers.



