# https://leetcode.com/problems/hamming-distance/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            # logical right shift
            xor = xor >> 1
        return distance

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance
