# 打印最深层次括号里的字符串。
def print_deepest_parentheses(s: str) -> list:
        max_depth = 0  # 记录最大深度
        current_depth = 0  # 当前深度
        current_content = []  # 临时存储当前括号内容
        result = []  # 存储最深层次的内容
        
        for char in s:
            if char == '(':
                current_depth += 1
                # 重置当前内容，准备记录新括号内的内容
                current_content = []
            elif char == ')':
                # 遇到右括号，说明当前括号内容结束
                if current_depth > max_depth:
                    # 发现更深层次，更新最大深度和结果
                    max_depth = current_depth
                    result = [''.join(current_content)]
                elif current_depth == max_depth:
                    # 同一深度，添加到结果
                    result.append(''.join(current_content))
                # 退出当前括号，深度减1
                current_depth -= 1
            else:
                # 普通字符，只有当处于括号内时才记录
                if current_depth > 0:
                    current_content.append(char)
        
        return result

# 测试示例
if __name__ == "__main__":
    test_cases = [
        "a(b(c)d)e",          # 输出: ['c']
        "a(b(c)d(e)f)g",      # 输出: ['c', 'e']
        "((a)b(c))",          # 输出: ['a', 'c']
        "abc(def)ghi",        # 输出: ['def']
        "((((test))))",       # 输出: ['test']
        "no parentheses here" # 输出: []
    ]
    
    for case in test_cases:
        print(f"输入: {case}")
        print(f"最深括号内容: {print_deepest_parentheses(case)}\n")


