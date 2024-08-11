# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            column = mid % n
            mid_el = matrix[row][column]
            if target == mid_el:
                return True
            if target < mid_el:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert (
        s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
    )
    assert s.searchMatrix([[1]], 1) == True
    assert s.searchMatrix([[1, 3]], 3) == True
    print("Done!")
