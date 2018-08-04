# https://leetcode.com/problems/single-number/description/

def single_number(nums)
  return nums[0] if nums.length == 1

  hash = {}
  nums.each do |el|
  	if hash[el].nil?
  	  hash[el] = true
  	elsif hash[el] == true
  	  hash[el] = false
  	end
  end

  hash.select{ |k, v| hash[k] }.keys[0]

end

def single_number_2(nums)
  require 'set'

  return nums[0] if nums.length == 1
  set = Set[]

  nums.each do |el|
    set.include?(el) ? set.delete(el) : set.add(el)
  end

  set.to_a[0]
end

def single_number_3(nums)
    result = 0
    nums.each do |value|
        result = result ^ value
    end
    
    result
end



p single_number_2([2,2,1])
p single_number_2([2,4,1,2,1])