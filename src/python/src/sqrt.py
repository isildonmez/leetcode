# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        higher, lower = x, 0
        while higher > lower + 1:
            divider = (higher + lower) // 2
            if divider**2 == x:
                return divider
            elif divider**2 > x:
                higher = divider
            else:
                lower = divider
        return lower


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.mySqrt(8) == 2
    print("Done!")
