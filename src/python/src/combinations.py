class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return res


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print("Done!")
