def max_sub_array2(nums)
  max = 0
  sum = 0
  for idx in 0...nums.length
    sum += nums[idx]
    sum = 0 if sum < 0
    max = sum if sum > max
  end
  return nums.max if nums.select{|num| num > 0}.empty?
  max
end

puts max_sub_array2([-2,1,-3,4,-1,2])
puts max_sub_array2([-2,1,-3,4,-1,-1,2,1,-4,-2])
puts max_sub_array2([-4,-2])

# 5
# 5
# -2