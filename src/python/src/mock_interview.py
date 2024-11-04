from typing import Optional

# Easy: Given an array of integers and a window size, write a function that returns the average value for each rolling window

# Example:
# Input = [1,2,3,4,5] int
# window_size = 3
# Output = [2.0,3.0,4.0]

# len(array)>0
# window_size<= len(array)
# return float array


def rolling_avg(nums: list[int], size: int) -> list[float]:
    result = []
    current_total = 0
    for i in range(size):
        current_total += nums[i]
    result.append(current_total / size)
    for i in range(1, len(nums) - size + 1):
        current_total -= nums[i - 1]
        current_total += nums[i + size - 1]
        result.append(current_total / size)
    return result


# 2

# Given an increasing sequence a[], we need to find the K-th missing element in the increasing sequence which is not present in the sequence.

# Input : a[] = {2, 3, 5, 9, 10, 11, 12};
#        k = 3;
# Output : 7

# Missing: {4,6,[7],8}

# a[] = {2, 4, 7, 8, 10, 11, 12}
#        0  1  2  3   4   5   6
# missing: 3 5 [6]

# medium


def missing_element(a: list[int], k: int) -> Optional[int]:
    if len(a) == 0:
        return None
    total_missing = a[-1] - a[0] - (len(a) - 1)
    if k > total_missing:
        return None
    left = 0
    right = len(a) - 1
    while right - left > 1:
        mid_idx = (left + right) // 2
        difference = a[mid_idx] - a[left]
        total_elements = mid_idx - left
        missing_elements = difference - total_elements
        if k <= missing_elements:
            right = mid_idx
        else:
            left = mid_idx
            k -= missing_elements
        mid_idx = (right + left) // 2
    difference = a[right] - a[left]
    total_elements = right - left
    missing_elements = difference - total_elements
    if missing_elements >= k:
        return a[left] + k


if __name__ == "__main__":
    print("Testing...")
    assert rolling_avg([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert missing_element([2, 3, 5, 9, 10, 11, 12], 3) == 7
    assert missing_element([2, 4, 7, 8, 10, 11, 12], 3) == 6
    assert missing_element([2, 4, 7, 8, 10, 11, 12], 10) is None
    assert missing_element([2, 4, 7, 8, 10, 11, 12, 15], 6) == 14
    assert missing_element([2, 5], 2) == 4
    assert missing_element([2, 5], 3) is None
    assert missing_element([], 3) is None
    print("Done!")
