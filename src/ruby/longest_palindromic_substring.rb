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