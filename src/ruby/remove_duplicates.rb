# def remove_duplicates(nums)
#   nums.uniq!
#   nums.length
# end

def remove_duplicates(nums)
  return nums.length if (nums.length <= 1)
  idx = 0
  length = 0
  while nums[idx]
    el = nums[idx]
    next_el = nums[idx+1]
    if (next_el) && (next_el == el)
        nums.delete_at(idx)
    else
      idx += 1
      length += 1
    end
  end
  nums.length
end

p remove_duplicates([1,2,2])
p remove_duplicates([])
p remove_duplicates([2,2,2,2])
p remove_duplicates([2,2,2,2,3,4,5,5,6])