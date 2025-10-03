'''
source: The interview question shared by classmates
run-length encoding of a single string
Definition：
    Encode：把连续相同字符压缩为“计数 + 字符”。
    Decode：把“计数 + 字符”展开还原为原串。
Example：
    Input：11122333455
        分段：111, 22, 333, 4, 55
        计数+字符：31 22 33 14 25 → 拼接为：3122331425
    Output：3122331425
Questions:
123
return [111213] or [123]?
'''
def encode_rle_digits(s: str) -> str:
    ans = []
    # [11122333455]
    #  l  r
    # two pointers
    n = len(s)
    # left: write ; right: read
    left = right = 0
    while right < n:
        while right < n and s[right] == s[left]:
            right += 1
        # points to different number
        length = right - left
        # record the frequency
        ans.append(str(length))
        # record the char
        ans.append(s[left])
        left = right
    return ''.join(ans)

def main():
    test_cases = [
        # (input, expected_output)
        ("11122333455", "3122331425"),  # given example
        ("12345", "1112131415"),        # each digit appears once
        ("1111", "41"),                 # single run
        ("", ""),                       # empty string
        ("22", "22"),                   # two of the same digit
        ("333221", "332211"),         # mixed runs
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = encode_rle_digits(inp)
        print(f"Test case {i}: input={inp}")
        print(f"Expected: {expected}")
        print(f"Got     : {result}")
        print("Pass    :", result == expected)
        print()


if __name__ == "__main__":
    main()