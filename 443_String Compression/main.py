'''
edge cases:
one char

variant: what if the input and output is int
'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        # 3 pointers (write + read)
        write = left = right = 0
        # replace the next digit of left pointer with number
        while right < n:
            while right < n and chars[right] == chars[left]:
                right += 1
            consecutive = right - left
            chars[write] = chars[left]
            if consecutive > 1:
                # only one char
                stringLength = str(consecutive)
                for c in stringLength:
                    write += 1
                    chars[write] = c
            write += 1
            left = right
        # return the length of the array with index of left pointer
        return write
