from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.chars = defaultdict(lambda: None)
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if not node.chars[c]:
                node.chars[c] = TrieNode()
            node = node.chars[c]
        node.is_end = True

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        is_found = False

        def dfs(node: TrieNode, i: int) -> None:
            nonlocal is_found
            # base case: 当前为 None 或者找到 last char
            if not node or is_found:
                return
            if i == len(word):
                if node and node.is_end:
                    is_found = True
                return
            # 如果是 '.' 就需要搜索所有 chars
            if word[i] != '.':
                dfs(node.chars[word[i]], i + 1)
            else:
                for nc, n_node in node.chars.items():
                    dfs(n_node, i + 1)

        dfs(self.root, 0)
        return is_found


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
