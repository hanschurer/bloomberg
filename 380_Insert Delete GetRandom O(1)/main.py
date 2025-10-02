'''
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''

# https://www.1point3acres.com/bbs/thread-1097351-1-1.html

import random

class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.idxs = {}

    def insert(self, val: int) -> bool:
        if val in self.idxs:
            return False
        idx = len(self.vals)
        self.vals.append(val)
        self.idxs[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idxs:
            return False
        idx = self.idxs.pop(val)
        if idx == len(self.vals) - 1:
            self.vals.pop()
        else:
            self.idxs[self.vals[-1]] = idx
            self.vals[idx] = self.vals[-1]
            self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#