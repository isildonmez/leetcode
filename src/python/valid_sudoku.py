# From https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

def valid_subpart(line: list[int]) -> bool:
    numerics = list(filter(lambda x: x.isnumeric(), line))
    numbers = list(map(lambda x: int(x), numerics))
    # Check if numbers are unique
    if len(numbers) != len(set(numbers)):
        return False
    # Check if numbers are in [1,9]
    if not set(numbers).issubset(set(range(1,10))):
        return False
    return True

def square_idx(r: int, c: int) -> int:
    return (r // 3) * 3 + (c // 3)

class Solution:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        sub_squares = [ [] for _ in range(9) ]
        for r in range(9):
            row = []
            column = []
            for c in range(9):
                row.append(board[r][c])
                column.append(board[c][r])
                sub_squares[square_idx(r, c)].append(board[r][c])
            if not valid_subpart(row) or not valid_subpart(column):
                return False
        for s in sub_squares:
            if not valid_subpart(s):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    b1 = [["5","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]
    b2 = [["8","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]
    print("Testing...")
    assert s.is_valid_sudoku(b1) == True
    assert s.is_valid_sudoku(b2) == False
    print("Done!")