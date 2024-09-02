def find_all_subsets(nums):
    subsets = [[]]
    for i in range(1, 2 ** len(nums)):
        subset = []
        for j in range(len(nums)):
            if include(i, j) == True:
                subset.append(nums[j])
        subsets.append(subset)
    return subsets


def include(pattern: int, idx: int) -> bool:
    if pattern & (1 << idx) == 0:
        return False
    return True
