# https://leetcode.com/problems/design-an-ordered-stream/description/

class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0 # 0-indexed 

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1 # 0-indexed 
        self.data[id] = value 
        if id > self.ptr: return [] # not reaching ptr 
        
        while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 # update self.ptr 
        return self.data[id:self.ptr]