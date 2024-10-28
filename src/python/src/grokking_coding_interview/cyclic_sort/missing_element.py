def find_missing_number(nums):
    i = 0
    while i < len(nums):
        if nums[i] != len(nums) and nums[i] != i:
            value = nums[i]
            nums[i], nums[value] = nums[value], nums[i]

        else:
            i += 1

    for i, n in enumerate(nums):
        if i != n:
            return i
    return len(nums)


if __name__ == "__main__":
    inputs = [
        [0, 1, 2, 4],
        [3, 0, 1, 4],
        [1, 4, 5, 6, 8, 2, 0, 7],
        [1, 0, 2, 3, 4, 5, 6, 8, 9, 7, 11],
        [1],
    ]
    results = [3, 2, 3, 10, 0]
    print("Testing...")
    for idx, input in enumerate(inputs):
        assert find_missing_number(input) == results[idx]
    print("Done!")
