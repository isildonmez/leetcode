# From https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150


def square_to_index(square: int, n: int) -> tuple[int, int]:
    steps = n**2 - square
    i = steps // n
    j = steps % n
    if (n - i) % 2 != 0:
        j = n - j - 1
    return (i, j)


def next_squares(board: list[list[int]], current_squares: set[int]) -> set[int]:
    n = len(board)
    next_squares = set()
    for current_square in current_squares:
        furthest_regular_square = None
        for s in range(current_square + 1, min(current_square + 6, n**2) + 1):
            i, j = square_to_index(s, n)
            val = board[i][j]
            if val != -1 and val != current_square:
                next_squares.add(val)
            elif val == -1 and (
                furthest_regular_square is None or furthest_regular_square < s
            ):
                furthest_regular_square = s
        if furthest_regular_square is not None:
            next_squares.add(furthest_regular_square)
    return next_squares


def check_min_num_of_move(
    board: list[list[int]],
    num_of_move: int,
    current_squares: set[int],
    visited_squares: set[int],
) -> int:
    squares = next_squares(board, current_squares)
    if not squares or squares.issubset(visited_squares):
        return -1
    num_of_move += 1
    n = len(board)
    if n**2 in squares:
        return num_of_move
    visited_squares.update(squares)
    return check_min_num_of_move(board, num_of_move, squares, visited_squares)


class Solution:
    def snakes_and_ladders(self, board: list[list[int]]) -> int:
        n = len(board)
        if n**2 < 7:
            return 1
        return check_min_num_of_move(board, 0, {1}, {1})

    def snakes_and_ladders_solution(self, board: list[list[int]]) -> int:
        oneDBoard = [
            num
            for index, row in enumerate(reversed(board))
            for num in row[:: (1 if index % 2 == 0 else -1)]
        ]

        boardLength = len(oneDBoard)
        queue = [(0, 1)]
        visited = [False] * boardLength

        dieSides = 6
        while queue:
            square, moves = queue.pop(0)
            for steps in range(1, dieSides + 1):
                moveTo = square + steps
                if oneDBoard[moveTo] != -1:
                    moveTo = oneDBoard[moveTo] - 1

                if moveTo == boardLength - 1:
                    return moves

                if not visited[moveTo]:
                    queue.append((moveTo, moves + 1))

                visited[moveTo] = True

        return -1


if __name__ == "__main__":
    s = Solution()
    b1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    b2 = [[-1, -1], [-1, 3]]
    b3 = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
    b4 = [
        [-1, 10, -1, 15, -1],
        [-1, -1, 18, 2, 20],
        [-1, -1, 12, -1, -1],
        [2, 4, 11, 18, 8],
        [-1, -1, -1, -1, -1],
    ]
    b5 = [[-1, 1, 1, 1], [-1, 7, 1, 1], [1, 1, 1, 1], [-1, 1, 9, 1]]
    print("Testing...")
    assert s.snakes_and_ladders(b1) == 4
    assert s.snakes_and_ladders(b2) == 1
    assert s.snakes_and_ladders(b3) == -1
    assert s.snakes_and_ladders(b4) == 3
    assert s.snakes_and_ladders(b5) == -1
    print("Done!")
