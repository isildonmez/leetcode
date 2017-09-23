def roman_to_int(s)
  hash = {I: 1, V: 5, X: 10, L: 50, C: 100,	D: 500,	M: 1000}
  result = 0

  for i in 0...s.size - 1
    current_int = hash[s[i].to_sym]
    next_int = hash[s[i + 1].to_sym]
    if current_int < next_int
      result -= current_int
    else
      result += current_int
    end
  end
  result += hash[s[-1].to_sym]
end


p roman_to_int("I")
p roman_to_int("III")
p roman_to_int("VII")
p roman_to_int("IX")
p roman_to_int("V")
p roman_to_int("MCMLIV")
p roman_to_int("MMXIV")


