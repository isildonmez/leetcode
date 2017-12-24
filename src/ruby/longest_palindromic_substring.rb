# Todo: Fix "abcda" split into 2 while loops.
def longest_palindrome_2(s)
  palindrome = true
  word = ""
  max = 0
  return s if s.length <= 1
  for idx in 0...s.length
    pos = 0
    pos_limit = [(idx+1), (s.length-idx)].min
    while (pos <= pos_limit)
      break if (s[idx-pos].nil? && s[idx+1+pos].nil? && !palindrome)
      if s[(idx)-pos] == s[idx+1+pos]
        substring = s[(idx-pos)..(idx+1+pos)]
        if substring.length > max
          word = substring
          max = substring.length
        end
        palindrome = true
      else
        palindrome = false
      end
      if s[idx-pos] == s[idx+pos]
        substring = s[(idx-pos)..(idx+pos)]
        if substring.length > max
          word = substring
          max = substring.length
        end
        palindrome = true
      else
        palindrome = false
      end
      pos += 1
    end
  end
  word
end

# p longest_palindrome_2("a")
# p longest_palindrome_2("ab")
# p longest_palindrome_2("aba")
p longest_palindrome_2("abcda")
# puts longest_palindrome_2("bababad")
# puts longest_palindrome_2("cbbd")
# puts longest_palindrome_2("cbad")



def longest_palindrome(s)
  arr = s.split("")
  hash = {}
  arr.each_with_index do |letter, idx|
    if hash[letter]
      hash[letter] << idx
    else
      hash[letter] = [idx]
    end
  end
  palindromes = []

  hash.each do |letter, index_array|
    if index_array.size > 1
      combinations = index_array.combination(2).to_a
      combinations.each do |idx_pairs|
        current_substring = s[idx_pairs[0]..idx_pairs[1]]
        substring = current_substring[1..-2]
        while (substring[0] == substring[-1]) &&
              (substring.length > 1)
          substring = substring[1..-2]
        end
        if substring.length <= 1
          palindromes << current_substring
        end
      end
    end
  end

  if palindromes.empty?
    return s[0]
  else
    return palindromes.max_by(&:length)
  end
end

puts longest_palindrome("bababad")
puts longest_palindrome("cbbd")
puts longest_palindrome("cbad")