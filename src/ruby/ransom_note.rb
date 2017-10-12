def can_construct(ransom_note, magazine)
  r_hash = {}
  m_hash ={}
  ransom_note.each_char do |char|
  	if r_hash.include? char
      r_hash[char] += 1
    else
      r_hash[char] = 1
    end
  end
  magazine.each_char do |char|
  	if m_hash.include? char
      m_hash[char] += 1
    else
      m_hash[char] = 1
    end
  end
  r_hash.each do |char, count|
    return false if m_hash[char].nil?
    return false if count > m_hash[char]
  end
  true
end

p can_construct("a", "b") #-> false
p can_construct("aa", "ab") #-> false
p can_construct("aa", "aab") #-> true
p can_construct("fffbfg", "effjfggbffjdgbjjhhdegh") #-> true

def alternative_can_construct(ransom_note, magazine)
    ransom_note.chars.uniq.each do |elm|
        return false unless ransom_note.count(elm) <= magazine.count(elm)
    end
    true
end

# This is the fastest code among leetcode solutions. But I could not understand why. Isn't it supposed to be O n2?