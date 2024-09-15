# https://leetcode.com/problems/nested-list-weight-sum/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        total = 0

        def current_depth_sum(depth: int, nl: list[NestedInteger]) -> int:
            nonlocal total
            for el in nl:
                if el.isInteger():
                    total += el.getInteger() * depth
                else:
                    current_depth_sum(depth + 1, el.getList())

        current_depth_sum(1, nestedList)
        return total


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.depthSum()
    print("Done!")
