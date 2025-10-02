from typing import Dict, List, Set, Deque
from collections import deque


class Solution:
    def __init__(self):
        self.adjList: Dict[str, List[str]] = {}
        self.currPath: List[str] = []
        self.shortestPaths: List[List[str]] = []

    def findNeighbors(self, word: str, wordSet: Set[str]) -> List[str]:
        neighbors: List[str] = []
        charList = list(word)
        for i in range(len(charList)):
            oldChar = charList[i]
            # replace the i-th character with all letters from a to z except the original character
            for c in "abcdefghijklmnopqrstuvwxyz":
                charList[i] = c
                newWord = "".join(charList)
                # skip if the character is same as original or if the word is not present in the wordSet
                if c == oldChar or newWord not in wordSet:
                    continue
                neighbors.append(newWord)
            charList[i] = oldChar
        return neighbors

    def backtrack(self, source: str, destination: str):
        # store the path if we reached the endWord
        if source == destination:
            tempPath = self.currPath.copy()
            tempPath.reverse()
            self.shortestPaths.append(tempPath)

        if source not in self.adjList:
            return

        for neighbor in self.adjList[source]:
            self.currPath.append(neighbor)
            self.backtrack(neighbor, destination)
            self.currPath.pop()

    def bfs(self, beginWord: str, endWord: str, wordSet: Set[str]):
        q: Deque[str] = deque([beginWord])
        # remove the root word which is the first layer in the BFS
        wordSet.discard(
            beginWord
        )  # discard does nothing if element is not found
        isEnqueued: Dict[str, bool] = {beginWord: True}
        while q:
            # visited will store the words of current layer
            visited: List[str] = []
            for _ in range(len(q)):
                currWord = q.popleft()
                # findNeighbors will have the adjacent words of the currWord
                neighbors = self.findNeighbors(currWord, wordSet)
                for neighbor in neighbors:
                    visited.append(neighbor)
                    if neighbor not in self.adjList:
                        self.adjList[neighbor] = []
                    # add the edge from neighbor to currWord in the list
                    self.adjList[neighbor].append(currWord)
                    if neighbor not in isEnqueued:
                        q.append(neighbor)
                        isEnqueued[neighbor] = True
            # removing the words of the previous layer
            for word in visited:
                wordSet.discard(word)

    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordSet: Set[str] = set(
            wordList
        )  # Use a set for efficient removal and checks
        # build the DAG using BFS
        self.bfs(beginWord, endWord, wordSet)

        # every path will start from the endWord
        self.currPath = [endWord]
        # traverse the DAG to find all the paths between endWord and beginWord
        self.backtrack(endWord, beginWord)

        return self.shortestPaths

