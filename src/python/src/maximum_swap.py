# https://leetcode.com/problems/maximum-swap/?envType=problem-list-v2&envId=a6ezkna5


import heapq


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits_to_latest_indices = {}
        max_heap = []
        digits = [int(n) for n in str(num)]
        for i, d in enumerate(digits):
            digits_to_latest_indices[d] = i
            heapq.heappush(max_heap, -d)
        pair_to_be_swapped = None
        for i, d in enumerate(digits):
            max_num = heapq.heappop(max_heap) * -1
            if d < max_num:
                idx = digits_to_latest_indices[max_num]
                pair_to_be_swapped = (idx, i)
                break
        if pair_to_be_swapped is not None:
            i1, i2 = pair_to_be_swapped
            digits[i1], digits[i2] = digits[i2], digits[i1]
            return int("".join([str(d) for d in digits]))
        return num


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.maximumSwap(2736) == 7236
    assert s.maximumSwap(9973) == 9973
    print("Done!")
