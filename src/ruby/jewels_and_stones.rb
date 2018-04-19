# https://leetcode.com/problems/jewels-and-stones/description/

def num_jewels_in_stones(j, s)
  h = {}
  result = 0
  s.split("").each do |stone|
    h[stone] ? h[stone] += 1 : h[stone] = 1
  end

  j.split("").each do |jewel|
    result += h[jewel] if h[jewel]
  end

  result
end

def num_jewels_in_stones2(j, s)
    s.count(j)
end