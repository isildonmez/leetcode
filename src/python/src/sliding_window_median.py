# https://leetcode.com/problems/sliding-window-median/submissions/1459051982/?envType=company&envId=datadog&favoriteSlug=datadog-all

import bisect


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        # Special cases: if k is 1, each element is its own median; if k is 2, use pairwise averages.
        if k == 1:
            return nums
        if k == 2:
            return [(nums[i] + nums[i + 1]) / 2 for i in range(len(nums) - 1)]

        is_odd = k % 2
        initial_window = sorted(nums[:k])

        # Initialize max heap for the lower half and min heap for the upper half
        max_heap = [-x for x in initial_window[: k // 2]]
        max_heap.reverse()
        min_heap = initial_window[k // 2 :]

        # Calculate the initial median
        if is_odd:
            result = [min_heap[0]]
        else:
            result = [(min_heap[0] - max_heap[0]) / 2]

        # Auxiliary heaps to mark elements to delete (for lazy deletion)
        max_heap_deletes, min_heap_deletes = [], []

        # Helper function to remove outdated elements from min_heap
        def clean_min_heap():
            while min_heap_deletes and min_heap_deletes[0] == min_heap[0]:
                heappop(min_heap_deletes)
                heappop(min_heap)

        # Helper function to remove outdated elements from max_heap
        def clean_max_heap():
            while max_heap_deletes and max_heap_deletes[0] == max_heap[0]:
                heappop(max_heap_deletes)
                heappop(max_heap)

        # Process each sliding window position
        for i in range(k, len(nums)):
            outgoing = nums[i - k]  # Element going out of the window
            incoming = nums[i]  # Element coming into the window
            current_median = min_heap[0]

            if outgoing >= current_median:
                # Outgoing element is in the upper half
                if incoming < current_median:
                    incoming = -heappushpop(max_heap, -incoming)
                    clean_max_heap()
                heappush(min_heap, incoming)
                heappush(min_heap_deletes, outgoing)
                clean_min_heap()
            else:
                # Outgoing element is in the lower half
                if incoming >= current_median:
                    incoming = heappushpop(min_heap, incoming)
                    clean_min_heap()
                heappush(max_heap, -incoming)
                heappush(max_heap_deletes, -outgoing)
                clean_max_heap()

            # Append the new median to the result list
            if is_odd:
                result.append(min_heap[0])
            else:
                result.append((min_heap[0] - max_heap[0]) / 2)

        return result


class Solution:
    def medianSlidingWindowNaive(self, nums: list[int], k: int) -> list[float]:
        idx = 0
        res = []
        window = None
        for idx in range(len(nums) - k + 1):
            if idx == 0:
                window = sorted(nums[idx : (k + idx)])
            else:
                window.remove(nums[idx - 1])
                bisect.insort(window, nums[idx + k - 1])
            if k % 2 == 0:
                total = window[k // 2] + window[k // 2 - 1]
                res.append(float(total / 2))
                total = 0
            else:
                res.append(float(window[k // 2]))
        return res
