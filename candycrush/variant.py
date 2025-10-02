# https://leetcode.com/discuss/post/7049289/bloomberg-sse-ny-phone-screen-full-loop-rpn92/

# Variant of candy crush
# "ABCCCBB" -> A
# "ABBBBBC" -> AC (notice here all 5 B are removed)


def candy_crush(s, k):
    stack = []

    for c in s:
        if stack and stack[-1][0]  == c:
            stack[-1][1] +=1
        else:
            while stack and stack[-1][1] > k:
                stack.pop()
            if stack and stack[-1][0] == c:
                stack[-1][1] +=1
            else:
                stack.append([c,1])
    #只有遇到不同的元素时才会pop 所以需要手动最后检查下 例子aabbccdd
    while stack and stack[-1][1]>k:
        stack.pop()
    
    return "".join(c for c, _ in stack)



print(candy_crush())