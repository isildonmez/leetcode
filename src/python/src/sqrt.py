# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 1, x // 2
        while left <= right:
            divider = (left + right) // 2
            if divider**2 == x:
                return divider
            if divider**2 > x:
                right = divider - 1
            else:
                left = divider + 1
        return right


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.mySqrt(8) == 2
    print("Done!")
