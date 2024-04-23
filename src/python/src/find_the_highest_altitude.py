# from https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
import itertools


class Solution:
    def largest_altitude(self, gain: list[int]) -> int:
        # n + 1 points
        # start at point 0, altitude == 0
        # len(gain) == n, gain[i] == -(points[i] - points[i+1])
        # points == [0, 1, ..., n]
        # altitude == [0, a1, ..., an]
        # gain == [a1-a0, a2-a1, ..., an - an-1]
        # return max(altitudes)
        # altitude == [0, gain[0], gain[0]+gain[1], gain[0]+gain[1] + gain[2], ..., gain[0] + ... + gain[n-1]]
        highest_next_altitude = max([0] + itertools.accumulate(gain))
        return max(highest_next_altitude, 0)


if __name__ == "__main__":
    print("Testing...")
    s = Solution()
    assert s.largest_altitude([-5, 1, 5, 0, -7]) == 1
    assert s.largest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0
    print("All passed")
