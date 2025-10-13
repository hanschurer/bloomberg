# 自創題： Given an input representing each node and its child, for example: NodeID: 1, child: 2; NodeID: 2, child: none; NodeID: 3, child: 1, find the root of the tree.

def find_root(nodes):
    # 收集所有节点ID和所有子节点ID
    all_node_ids = set()
    child_ids = set()
    
    for node_id, child in nodes:
        all_node_ids.add(node_id)
        if child is not None:  # 子节点存在时才添加
            child_ids.add(child)
    
    # 根节点是唯一在all_node_ids中但不在child_ids中的节点
    root = (all_node_ids - child_ids).pop()
    return root

# 示例用法
if __name__ == "__main__":
    # 输入格式：[(节点ID, 子节点ID), ...]，子节点为None表示无
    nodes = [
        (1, 2),
        (2, None),
        (3, 1)
    ]
    print(find_root(nodes))  # 输出：3（因为3没有父节点）
