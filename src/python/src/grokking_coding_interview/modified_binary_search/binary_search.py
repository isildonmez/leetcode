def binary_search(nums, target):
    mid_idx = len(nums) // 2
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[mid_idx] == target:
            return mid_idx
        if nums[mid_idx] < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
        mid_idx = (left + right) // 2
    return -1
