def longest_common_prefix(strs)
  if strs != []
    prefix = strs.min_by(&:length)
    while prefix != ""
      return prefix if strs.all?{|str| str[0...prefix.length] == prefix}
      prefix = prefix.chop
    end
  end
  return ""
end

p longest_common_prefix(["a", "ab","abcd"]) # "a"
p longest_common_prefix(["", "abc", "abc"]) # ""
p longest_common_prefix(["ab", "ab"]) # "ab"
p longest_common_prefix(["abc", "cabc"]) # ""
p longest_common_prefix([]) # ""
