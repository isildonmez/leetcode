def merge_sorted(nums1, m, nums2, n):
    i1 = m - 1
    i2 = n - 1
    i = m + n - 1
    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[i] = nums1[i1]
            i1 -= 1
        else:
            nums1[i] = nums2[i2]
            i2 -= 1
        i -= 1
    if i1 < 0:
        nums1[: i + 1] = nums2[: i + 1]
    return nums1
