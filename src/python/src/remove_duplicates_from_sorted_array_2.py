class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2: return len(nums)
        insert_idx = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[i-1] or nums[i] != nums[insert_idx-2]:
                nums[insert_idx] = nums[i]
                insert_idx += 1
        return insert_idx

    def remove_duplicates_alternative(self, nums: list[int]) -> int:
        removed = []
        for n in nums:
            if len(removed) >= 2 and removed[-2] == n:
                continue
            removed.append(n)
            print(removed)
        for i, n in enumerate(removed):
            nums[i] = n
        return len(removed)
    
if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.remove_duplicates([1,1,1,2,2,3]) == 5
    assert s.remove_duplicates([0,0,1,1,1,1,2,3,3]) == 7
    print("Done!")