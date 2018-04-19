# https://leetcode.com/problems/hamming-distance/description/

def hamming_distance(x, y)
  def turn_into_bits(int)
    new_int = 0
    digit = 0
    while int > 0
      remainder = int % 2
      int /= 2
      new_int += (remainder * (10**digit))
      digit += 1
    end
    new_int
  end

  a = turn_into_bits(x)
  b = turn_into_bits(y)
  higher = [a, b].max
  lower = higher == a ? b : a

  zipped_array = higher.digits.zip(lower.digits)

  ham_distance = 0
  zipped_array.each do |arr|
    ham_distance += 1 if (arr.map{|el| el ? el : 0}.uniq.size != 1)
  end

  ham_distance
end

# According to ruby's bitwise operators(https://www.calleerlandsson.com/rubys-bitwise-operators/):
def hamming_distance2(x,y)
  (x ^ y).to_s(2).split("").select{|el| el == "1"}.length
  # or
  # (x^y).to_s(2).split('').reduce(0){|s, e| s += e.to_i}
  # or
  # (x^y).to_s(2).count("1")
end