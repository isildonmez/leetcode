class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        i = j = 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.remove_duplicates([1, 1, 1, 2, 2, 3]) == 5
    assert s.remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
    print("Done!")
