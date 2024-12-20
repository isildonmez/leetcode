# https://leetcode.com/problems/height-checker/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        num_of_ind = 0
        for h, e in zip(heights, sorted(heights)):
            if h != e:
                num_of_ind += 1
        return num_of_ind
