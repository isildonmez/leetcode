#  from https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        number_of_zeroes = 0
        while True:
            try:
                nums.remove(0)
                number_of_zeroes += 1
            except ValueError:
                break
        nums += [0] * number_of_zeroes
        return nums

    def refactored_move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        idx = 0
        for n in nums:
            if n == 0:
                count_zero += 1
            else:
                nums[idx] = n
                idx += 1
        nums[idx:] = [0] * count_zero


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert s.move_zeroes([0]) == [0]
    print("All passed")
