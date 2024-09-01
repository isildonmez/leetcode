def jump_game(nums):
    target_idx = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= target_idx - i:
            target_idx = i
    if target_idx == 0:
        return True
    return False
