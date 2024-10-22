import random


# On^2 (Worst and avg case), On (Best)
# O1 (Space)
def bubble_sort(nums: list[int]) -> list[int]:
    last_unsorted_idx = len(nums) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(last_unsorted_idx):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
        last_unsorted_idx -= 1
    return nums


# Onlogn
# On (Space)
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    mid_idx = len(nums) // 2
    left, right = nums[:mid_idx], nums[mid_idx:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


# Onlogn (Best and avg) On^2 (worst)
# On (Space)
def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    idx = random.randint(0, len(nums) - 1)
    pivot = nums[idx]
    smaller = [i for i in nums[:idx] + nums[idx + 1 :] if i <= pivot]
    greater = [i for i in nums[:idx] + nums[idx + 1 :] if i > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)


# On^2 (Best, Worst, Avg)
# O1 (Space)
def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums


# On^2 (Avg, Worst), On(Best)
# O1 (Space)
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums


if __name__ == "__main__":
    nums1 = [3, 5, 1, 2, 3]
    nums2 = []
    nums3 = [5, 5, 4, 3, 2, 1, 5]
    print("Testing...")
    assert bubble_sort(nums1) == [1, 2, 3, 3, 5]
    assert bubble_sort(nums2) == []
    assert bubble_sort(nums3) == [1, 2, 3, 4, 5, 5, 5]
    assert merge_sort(nums1) == [1, 2, 3, 3, 5]
    assert merge_sort(nums2) == []
    assert merge_sort(nums3) == [1, 2, 3, 4, 5, 5, 5]
    assert quick_sort(nums1) == [1, 2, 3, 3, 5]
    assert quick_sort(nums2) == []
    assert quick_sort(nums3) == [1, 2, 3, 4, 5, 5, 5]
    assert selection_sort(nums1) == [1, 2, 3, 3, 5]
    assert selection_sort(nums2) == []
    assert selection_sort(nums3) == [1, 2, 3, 4, 5, 5, 5]
    assert insertion_sort(nums1) == [1, 2, 3, 3, 5]
    assert insertion_sort(nums2) == []
    assert insertion_sort(nums3) == [1, 2, 3, 4, 5, 5, 5]
    print("Done!")
