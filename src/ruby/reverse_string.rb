# https://leetcode.com/problems/reverse-string/description/

def reverse_string(s)
	size = s.length
	return s if size < 2

	result = ''
	(size-1).downto(0) do |idx|
		result << s[idx]
	end

	result
end

def reverse_string2(s)
    s.reverse
end

p reverse_string('hello')