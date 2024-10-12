import heapq


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits_to_latest_indices = {}
        max_heap = []
        digits = [int(n) for n in str(num)]
        for i, d in enumerate(digits):
            digits_to_latest_indices[d] = i
            heapq.heappush(max_heap, -d)
        res = digits.copy()
        for i, d in enumerate(digits):
            max_num = heapq.heappop(max_heap) * -1
            if d < max_num:
                idx = digits_to_latest_indices[max_num]
                res[i], res[idx] = max_num, d
                return int("".join([str(d) for d in res]))
        return num


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.maximumSwap(2736) == 7236
    assert s.maximumSwap(9973) == 9973
    print("Done!")
