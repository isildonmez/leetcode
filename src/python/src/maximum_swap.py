from collections import defaultdict


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = str(num)
        idx_by_digits = defaultdict(set)
        for idx, d in enumerate(nums):
            idx_by_digits[int(d)].add(idx)
        digits = set(idx_by_digits.keys())
        for _ in range(len(digits)):
            highest_digit = max(digits)
            highest_idx = max(idx_by_digits[highest_digit])
            for i in range(highest_idx):
                if int(nums[i]) < highest_digit:
                    return int(
                        nums[:i]
                        + str(highest_digit)
                        + nums[i + 1 : highest_idx]
                        + nums[i]
                        + nums[highest_idx + 1 :]
                    )
            digits -= {highest_digit}
        return num


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.maximumSwap(2736) == 7236
    assert s.maximumSwap(9973) == 9973
    print("Done!")
