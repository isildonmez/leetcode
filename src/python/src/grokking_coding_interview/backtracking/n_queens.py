def solve_n_queens(n):
    possibilities = 0
    queens = []

    def place_a_queen(row: int):
        nonlocal possibilities
        if row == n:
            possibilities += 1
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))
                place_a_queen(row + 1)
                queens.pop()

    place_a_queen(0)
    return possibilities


def is_safe(row: int, col: int, queens: list[tuple[int, int]]):
    for r, c in queens:
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True


if __name__ == "__main__":
    print("Testing...")
    assert solve_n_queens(4) == 2
    assert solve_n_queens(6) == 4
    print("Done!")
