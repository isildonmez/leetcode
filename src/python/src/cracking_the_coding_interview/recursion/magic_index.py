from typing import Optional


def magic_index(nums: list[int]) -> Optional[int]:
    if len(nums) == 0:
        return None
    left, right = 0, len(nums) - 1
    if nums[left] == left:
        return left
    if nums[right] == right:
        return right
    while left < right:
        mid_idx = (left + right) // 2
        if nums[mid_idx] == mid_idx:
            return mid_idx
        if nums[mid_idx] > mid_idx:
            right = mid_idx - 1
        else:
            left = mid_idx + 1
    return None


if __name__ == "__main__":
    print("Testing...")
    assert magic_index([-9, -7, -5, 3]) == 3
    assert magic_index([-9, -7, -5, 5, 6]) == None
    assert magic_index([-9, -7, -5, 3, 5]) == 3
    print("Done!")
