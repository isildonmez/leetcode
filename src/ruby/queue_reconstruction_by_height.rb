# https://leetcode.com/problems/queue-reconstruction-by-height/description/
# start placing highest ones first.

def reconstruct_queue(people)
  people_hash = {}
  people.each do |individual|
    if people_hash.include? (individual[0])
      people_hash[individual[0]] << individual[1]
    else
      people_hash[individual[0]] = [individual[1]]
    end
  end
  people_hash.transform_values{|k_array| k_array.sort!}
  heights_inc = people_hash.keys.sort_by!{|el| el}

  queue = []
  highest_el = heights_inc.pop

  while highest_el
    k_array = people_hash[highest_el]
    k_array.each do |idx|
      queue.insert(idx, [highest_el, idx])
    end
    highest_el = heights_inc.pop
  end
  queue
end