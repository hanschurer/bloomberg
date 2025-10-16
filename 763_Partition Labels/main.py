# https://www.1point3acres.com/bbs/thread-1121985-1-1.html
from typing import List

def partitionLabels(s: str) -> List[int]:
    """
    使用贪心算法划分字母区间
    """
    # 1. 预处理：统计每个字母的最后出现位置
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    result = []
    partition_start = 0
    partition_end = 0
    
    # 2. 遍历与划分
    for i, char in enumerate(s):
        # 更新当前片段需要到达的最远边界
        partition_end = max(partition_end, last_occurrence[char])
        
        # 如果当前索引已经到达了最远边界，说明可以进行划分
        if i == partition_end:
            length = partition_end - partition_start + 1
            result.append(length)
            
            # 更新下一个片段的起始点
            partition_start = i + 1
            
    return result

# --- 测试 ---
s = "ababcbacadefegdehijhklij"
print(f"输入: {s}")
print(f"输出: {partitionLabels(s)}") # 应该输出 [9, 7, 8]

s2 = "eccbbbbdec"
print(f"输入: {s2}")
print(f"输出: {partitionLabels(s2)}") # 应该输出 [10]