import heapq


class KthLargest:
    def __init__(self, k, nums):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums
        self.k = k

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) < self.k:
            return
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
