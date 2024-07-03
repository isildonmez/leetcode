# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.


class MyStack:
    def __init__(self, l: list):
        self.list = l
        self.min_val = min(l)

    def push(self, el: int) -> None:
        self.list.append(el)
        self.min_val = min(self.min_val, el)

    def pop(self) -> int:
        popped = self.list.pop()
        if min(popped, self.min_val) == popped:
            self.min_val = min(self.list)
        return popped

    def min(self) -> int:
        return self.min_val
