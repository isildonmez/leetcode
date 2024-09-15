# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.multipliers = {}
        for i, n in enumerate(self.nums):
            if n != 0:
                self.multipliers[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for idx, num in self.multipliers.items():
            res += num * vec.nums[idx]
        return res
