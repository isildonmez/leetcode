# https://leetcode.com/problems/counting-bits/description/

def count_bits(num)
    sub_nums = []
    for i in 0..num
    	sub_nums << i
    end

    sub_nums.map{|i| i.to_s(2)}.map do |i|
			i.count "1"
    end
end