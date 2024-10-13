# From https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, idx = m - 1, n - 1, m + n - 1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[idx] = nums1[i1]
                i1 -= 1
            else:
                nums1[idx] = nums2[i2]
                i2 -= 1
            idx -= 1


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert s.merge([1], 1, [], 0) == [1]
    assert s.merge([0], 0, [1], 1) == [1]
    assert s.merge_refactor([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert s.merge_refactor([1], 1, [], 0) == [1]
    assert s.merge_refactor([0], 0, [1], 1) == [1]
    assert s.merge_refactor([2, 0], 1, [1], 1) == [1, 2]
    assert s.merge_refactor([1, 2, 4, 5, 6, 0], 5, [3], 1) == [1, 2, 3, 4, 5, 6]
    assert s.merge_refactor([1, 2, 4, 6, 7, 0], 5, [3, 5], 2) == [1, 2, 3, 4, 5, 6, 7]
    assert s.merge_refactor([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6]
