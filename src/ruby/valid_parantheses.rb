def is_valid(s)
  return false if s.length.odd?
  new_string = s
  keep_going = true
  while keep_going
  	control = new_string
    ['()','{}','[]'].each do |chr|
      new_string = new_string.split(chr).join
    end
    control = new_string ? keep_going = false : keep_going = true
  end
  new_string = "" ? true : false
end

p is_valid('(){}[]')
p is_valid('({})')
p is_valid('({[[({})]]})')
p is_valid('({[[({]})]]})')


# A solution I find the best practice:
def is_valid_2(str)
  stack = []

  return false unless str.length % 2 == 0

  str.each_char do |c|
    case c
      when '{', '(', '['
        stack << c
      when '}'
        return false unless stack.pop == '{'
      when ')'
        return false unless stack.pop == '('
      when ']'
        return false unless stack.pop == '['
    end
  end
  stack.empty?
end