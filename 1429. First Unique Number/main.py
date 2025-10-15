
class FirstUnique:

    def __init__(self, nums):
        self.counts = Counter(nums)
        self.que = deque(nums)

    def showFirstUnique(self) -> int:
        while self.que and self.counts[self.que[0]] > 1:
            self.que.popleft()
        if self.que:
            return self.que[0]
        return -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        self.que.append(value)

