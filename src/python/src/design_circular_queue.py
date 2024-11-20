# https://leetcode.com/problems/design-circular-queue/description/?envType=company&envId=datadog&favoriteSlug=datadog-all


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.que = [None] * self.size
        self.current = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull() is True:
            return False
        self.que[self.current] = value
        self.current += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() is True:
            return False
        self.que = self.que[1:]
        self.que.append(None)
        self.current -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.que[0]

    def Rear(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.que[self.current - 1]

    def isEmpty(self) -> bool:
        if self.current == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.current == self.size:
            return True
        return False
