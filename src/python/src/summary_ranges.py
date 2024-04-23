class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        result = []
        idx = 0
        while idx < len(nums):
            start, end = idx, idx
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1] - 1:
                end = idx + 1
                idx += 1
            if start == end:
                result.append(f"{nums[start]}")
            else:
                result.append(f"{nums[start]}->{nums[end]}")
            idx += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    # assert s.summary_ranges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
    print("Done!")
