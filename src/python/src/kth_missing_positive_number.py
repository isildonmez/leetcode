# https://leetcode.com/problems/kth-missing-positive-number/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid_idx = (left + right) // 2
            missing = arr[mid_idx] - mid_idx - 1
            if missing < k:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        return k + left
