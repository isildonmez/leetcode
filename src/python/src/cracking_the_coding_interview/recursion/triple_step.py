from typing import Optional


def triple_step(n: int) -> int:
    if n == 0:
        return 0
    paths = [None] * (n + 1)
    return count_paths(n, paths)


def count_paths(n: int, paths: list[Optional[int]]) -> int:
    if n == 0:
        return 1
    elif paths[n] is not None:
        return paths[n]
    else:
        if n >= 1:
            paths[n] = 0
            paths[n] += count_paths(n - 1, paths)
        if n >= 2:
            paths[n] += count_paths(n - 2, paths)
        if n >= 3:
            paths[n] += count_paths(n - 3, paths)
        return paths[n]


if __name__ == "__main__":
    print("Testing...")
    assert triple_step(1) == 1
    assert triple_step(2) == 2
    assert triple_step(3) == 4
    assert triple_step(4) == 7
    print("Done!")
