def binary_search(nums, target):
    mid_idx = len(nums) // 2
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[mid_idx] == target:
            return mid_idx
        if nums[mid_idx] < target:
            l = mid_idx + 1
        else:
            r = mid_idx - 1
        mid_idx = (l + r) // 2
    return -1
