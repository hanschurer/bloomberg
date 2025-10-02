class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # calculate the distance between two words using recursion
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

    def minDistanceRecur(
        self, word1: str, word2: str, word1Index: int, word2Index: int
    ) -> int:
        # base cases
        if (
            word1Index == 0
        ):  # if word1 is empty, the minimum distance is the length of word2
            return word2Index
        if (
            word2Index == 0
        ):  # if word2 is empty, the minimum distance is the length of word1
            return word1Index
        # if the characters are same, continue with next pair of characters
        if word1[word1Index - 1] == word2[word2Index - 1]:
            return self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index - 1
            )
        else:
            # calculate the cost of insert, delete, and replace operations
            insertOperation = self.minDistanceRecur(
                word1, word2, word1Index, word2Index - 1
            )
            deleteOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index
            )
            replaceOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index - 1
            )
            # return the minimum cost
            return min(insertOperation, deleteOperation, replaceOperation) + 1
