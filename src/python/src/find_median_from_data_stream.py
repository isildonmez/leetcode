# https://leetcode.com/problems/find-median-from-data-stream/description/?envType=company&envId=spotify&favoriteSlug=spotify-all


import bisect
import heapq


class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        n = heapq.heappop(self.low)
        heapq.heappush(self.high, -n)

        if len(self.low) < len(self.high):
            n = heapq.heappop(self.high)
            heapq.heappush(self.low, -n)

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return float((-self.low[0] + self.high[0]) / 2)
        return float(-self.low[0])


# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
class MedianFinder:
    def __init__(self):
        self.count = [0] * 101  # Array to count occurrences of each number
        self.total = 0  # Total count of numbers

    def addNum(self, num: int) -> None:
        self.count[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        if self.total == 0:
            return 0

        # If total is odd, find the middle number
        # If total is even, find the two middle numbers
        count = 0
        mid = self.total // 2

        # For odd count
        if self.total % 2 == 1:
            for i in range(101):
                count += self.count[i]
                if count > mid:
                    return float(i)
        # For even count
        else:
            first = None
            for i in range(101):
                count += self.count[i]
                if first is None and count > mid - 1:
                    first = i
                if count > mid:
                    return (first + i) / 2


# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
class MedianFinder:
    def __init__(self):
        self.count = [0] * 101  # For numbers in [0,100]
        self.outliers = []  # For numbers outside range
        # min_heap and max_heap can be used here as well.
        self.total = 0

    def addNum(self, num: int) -> None:
        if 0 <= num <= 100:
            self.count[num] += 1
        else:
            bisect.insort(self.outliers, num)
        self.total += 1

    def findMedian(self) -> float:
        if self.total == 0:
            return 0

        mid = self.total // 2
        regular_nums = sum(self.count)

        # Function to get nth number across both regular and outlier numbers
        def get_nth(n):
            count = 0
            # Check regular numbers first
            for i in range(101):
                count += self.count[i]
                if count > n:
                    return i
            # If not found, look in outliers
            return self.outliers[n - (regular_nums)]

        if self.total % 2 == 1:
            return float(get_nth(mid))
        else:
            return (get_nth(mid - 1) + get_nth(mid)) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
