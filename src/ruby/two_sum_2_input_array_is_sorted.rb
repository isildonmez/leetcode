def two_sum(numbers, target)
  limit = target / 2

  hash_of_numbers = {}
  numbers.each_with_index do |num, idx|
    hash_of_numbers[num] = idx
  end

  numbers.each_with_index do |num, idx|
    if num <= limit && hash_of_numbers.include?(target - num)
      return [idx + 1, hash_of_numbers[target - num] + 1]
    end
  end
end

p two_sum([2,7,11,15], 9)
p two_sum([0,0,3,4], 0)