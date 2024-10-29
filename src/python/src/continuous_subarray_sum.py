# https://leetcode.com/problems/continuous-subarray-sum/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mod_seen = {0: -1}
        prefix_mod = 0
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                idx = mod_seen[prefix_mod]
                if i - idx > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False
