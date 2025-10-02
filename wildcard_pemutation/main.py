# https://leetcode.com/discuss/post/7049289/bloomberg-sse-ny-phone-screen-full-loop-rpn92/
# write iterative approach for the given binary string with wildcard "?" where wildcard can be replace with 0 or 1.
# Return all permutations by replacing the wildcard character
# e.g.
# "0?" -> "00", "01"
# "0?1" -> "001", "011"
# "0??1" -> "0001", "0011", "0101", "0111"


def wildcard_pemutations(s:str)->list[str]:
    res = []
    n = len(s)
    def dfs(i, path):
        if i == len(s):
            res.append("".join(path))
            return
        
        if s[i] == "?":
            path.append('0')
            dfs(i+1, path)
            path.pop()

            path.append('1')
            dfs(i+1,path)
            path.pop()
        else:
            path.append(s[i])
            dfs(i+1,path)
            path.pop()
        
    
    dfs(0, [])
    return res 


print(wildcard_pemutations("0?"))
print(wildcard_pemutations("0?1"))
print(wildcard_pemutations("0??1"))