class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: drop invalid ')' starting from the start- Pass 1 guarantees we never keep a ) without an earlier matching (.
        # aka. keep ) only if it has a preceding unmatched ( (tracked by balance). Because we only keep ) when there’s a preceding unmatched (, 
        # every kept ) is matched by some earlier ( at that point. Therefore, after Pass 1, the buffer contains no unmatched ).
        # The only possible mismatches left are some ( (exactly balance of them), because we never over-accepted ).
        buf = []
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
                buf.append(ch)
            elif ch == ')':
                if balance == 0:
                    continue  # skip this unmatched ')' in our result
                balance -= 1
                buf.append(ch)
            else:   # normal char
                buf.append(ch)

        # Pass 2: drop extra '(' starting from the end - Pass 2 cleans up the leftover opens so every ( gets a matching ).
        # aka. We traverse right→left and delete exactly balance occurrences of (. We removed all leftover unmatched (
        res = []
        open_to_remove = balance  # number of unmatched '(' remaining
        for ch in reversed(buf):
            if ch == '(' and open_to_remove > 0:
                open_to_remove -= 1  # drop this '('
            else:
                res.append(ch)

        return ''.join(reversed(res))
    
# tc: O(n)
# sc: O(n) -> buffer