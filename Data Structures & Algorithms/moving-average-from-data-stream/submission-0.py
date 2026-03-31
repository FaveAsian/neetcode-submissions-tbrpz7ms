class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stream = deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.stream) >= self.size:
            popped_val = self.stream.popleft()
            self.total -= popped_val
        
        self.stream.append(val)
        self.total += val
        return self.total/len(self.stream)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
