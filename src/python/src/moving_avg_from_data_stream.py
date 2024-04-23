from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            outgroup = self.window.popleft()
            self.sum -= outgroup
        self.window.append(val)
        self.sum += val
        return self.sum / len(self.window)


if __name__ == "__main__":
    print("Testing...")
    m = MovingAverage(3)
    assert m.next(1) == 1.0
    assert m.next(10) == 5.5
    assert m.next(3) == 14 / 3
    assert m.next(5) == 6.0
    print("Done!")
