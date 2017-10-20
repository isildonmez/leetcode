def contains_duplicate(nums)
  require 'set'

  s = Set.new
  nums.each do |el|
    if s.include? el
      return true
    else
      s << el
    end
  end
  false
end

def alternative_contains_duplicate(nums)
  !(nums == nums.uniq)
end