def title_to_number(s)
  if s.size == 1
    column_no = s.ord - 64
  else
    column_no = title_to_number(s[-1])
    column_no += title_to_number(s[0]) * 26
  end
  column_no
end

puts title_to_number("A") # 1
puts title_to_number("B") # 2
puts title_to_number("Z") # 26
puts title_to_number("AA") # 27


def title_to_number(s)
  column_no = 0
  digit = s.length - 1
  digit.downto(0) do |i|
    column_no += (s[digit - i].ord - 64) * (26 ** i)
  end
  column_no
end