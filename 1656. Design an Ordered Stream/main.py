# https://leetcode.com/problems/design-an-ordered-stream/description/
# Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")

# Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
# You cannot queue up the incoming data from the stream.
# So for example if the first incoming bit of data is (1, "abcd"), and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.
# class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0 # 0-indexed 

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1 # 0-indexed 
        self.data[id] = value 
        if id > self.ptr: return [] # not reaching ptr 
        
        while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 # update self.ptr 
        return self.data[id:self.ptr]