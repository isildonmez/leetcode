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
    l = 0
    r = len(a) - 1
    while r - l > 1:
        mid_idx = (l + r) // 2
        difference = a[mid_idx] - a[l]
        total_elements = mid_idx - l
        missing_elements = difference - total_elements
        if k <= missing_elements:
            r = mid_idx
        else:
            l = mid_idx
            k -= missing_elements
        mid_idx = (r + l) // 2
    difference = a[r] - a[l]
    total_elements = r - l
    missing_elements = difference - total_elements
    if missing_elements >= k:
        return a[l] + k


if __name__ == "__main__":
    print("Testing...")
    assert rolling_avg([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert missing_element([2, 3, 5, 9, 10, 11, 12], 3) == 7
    assert missing_element([2, 4, 7, 8, 10, 11, 12], 3) == 6
    assert missing_element([2, 4, 7, 8, 10, 11, 12], 10) == None
    assert missing_element([2, 4, 7, 8, 10, 11, 12, 15], 6) == 14
    assert missing_element([2, 5], 2) == 4
    assert missing_element([2, 5], 3) == None
    assert missing_element([], 3) == None
    print("Done!")
