def max_sub_array(nums)
  max = 0
  subarray = nums
  sum = 0

  neg_idx = subarray.find_index{|num| num < 0 }
  until neg_idx.nil?
    sum += subarray[0...neg_idx].sum
    max = sum if sum > max
    sum += subarray[neg_idx]
    sum = 0 if sum < 0
    subarray = subarray[(neg_idx+1)..-1]
    neg_idx = subarray.find_index{|num| num < 0 }
  end
  sum += subarray.sum
  [sum, max].max
end

puts max_sub_array([-2,1,-3,4,-1,2])
puts max_sub_array([-2,1,-3,4,-1,-1,2,1,-4,-2,6])