# https://leetcode.com/problems/fizz-buzz/description/

def fizz_buzz(n)
	result = []

	for i in 1..n
		case
		when i % 15 == 0
			result << "FizzBuzz"
		when i % 3 == 0
			result << "Fizz"
		when i % 5 == 0
			result << "Buzz"
		else
			result << i.to_s
		end
	end
  result
end